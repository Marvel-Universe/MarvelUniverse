import os
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from ..models.quiz_models import CharacterQuestion, CharacterChoice
from django.core.management import call_command
from ..models.user_data_models import UserData

class SelectQuizViewTest(TestCase):
    """
    Test suite for the SelectQuizView in the Marvel Universe quiz application.

    This test suite ensures that the SelectQuizView behaves as expected, including
    verifying the response status code and the correct template usage.
    """
    def setUp(self):
        """
        Set up method for SelectQuizViewTest. This method is run before each test.
        It loads necessary data and initializes the test client.
        """
        call_command('loaddata', os.getcwd() + '/data/google-oauth-data.json', '--exclude=contenttypes')
        self.client = Client()

    def test_select_quiz_view_get(self):
        """
        Test the GET request response of SelectQuizView.
        This test checks if the view returns a 200 status code and uses the correct template.
        """
        response = self.client.get(reverse('MarvelUniverse:select-quiz'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'MarvelUniverse/quiz/select-quiz.html')


class CharacterQuizViewTest(TestCase):
    """
    Test suite for the CharacterQuizView in the Marvel Universe quiz application.

    This suite tests various scenarios including valid and invalid GET requests,
    and POST requests with correct choices.
    """
    def setUp(self):
        """
        Set up method for CharacterQuizViewTest. This method is run before each test.
        It initializes the test data and the test client.
        """
        self.client = Client()
        self.user = User.objects.create_user(username='Sanquiz', email='sanquiz@example.com', password='sanquiz1234')

        # Create test data for CharacterQuestion and CharacterChoice
        self.question = CharacterQuestion.objects.create(description='This guy was born green')
        self.correct_choice = CharacterChoice.objects.create(question=self.question, character_name='Hulk', is_correct=True)
        self.incorrect_choices = [
            CharacterChoice.objects.create(question=self.question, character_name=f'Incorrect Character {i}', is_correct=False) for i in range(3)]
        self.url = reverse('MarvelUniverse:character-quiz', args=[self.question.id])

    def test_valid_get_request(self):
        """
        Test a valid GET request to the CharacterQuizView.
        Checks if the view responds with status 200 and uses the correct template.
        """
        self.client.login(username='Sanquiz', password='sanquiz1234')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'MarvelUniverse/quiz/character-quiz.html')

    def test_get_request_with_invalid_question(self):
        """
        Test a GET request to CharacterQuizView with an invalid question ID.
        Verifies if the view redirects to the select quiz page when an invalid question is requested.
        """
        self.client.login(username='Sanquiz', password='sanquiz1234')
        invalid_url = reverse('MarvelUniverse:character-quiz', args=[999])
        response = self.client.get(invalid_url)
        self.assertRedirects(response, reverse('MarvelUniverse:select-quiz'))

    def test_post_request_with_correct_choice(self):
        """
        Test a POST request to CharacterQuizView with a correct choice.
        Checks if the session data is updated correctly and verifies the expected behavior.
        """
        self.client.login(username='Sanquiz', password='sanquiz1234')
        session = self.client.session
        session['question_counter'] = 0
        session['scores_per_game'] = 0
        session.save()
        response = self.client.post(self.url, {'choice_id': self.correct_choice.id}, follow=True)
        self.assertEqual(self.client.session['question_counter'], 1)
        self.assertEqual(self.client.session['scores_per_game'], 50)


class LeaderboardViewTest(TestCase):
    """
    Test suite for the LeaderboardView in the Marvel Universe quiz application.

    This suite tests the leaderboard view functionality including the updating of user scores
    and the rendering of the leaderboard with accurate context data.
    """
    def setUp(self):
        """
        Set up method for LeaderboardViewTest. This method is run before each test.
        It creates test users and their associated UserData for leaderboard testing.
        """
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        UserData.objects.create(user=self.user, scores=0)

        for i in range(4):
            user = User.objects.create_user(username=f'user{i}', email=f'user{i}@example.com', password='password')
            UserData.objects.create(user=user, scores=(i + 1) * 100)

        self.url = reverse('MarvelUniverse:leaderboard')

    def test_leaderboard_with_scores_in_session(self):
        """
        Test the LeaderboardView when there are scores in the session.
        Verifies that user scores are updated correctly and that the leaderboard context is accurate.
        """
        self.client.login(username='testuser', password='password')
        session = self.client.session
        session['scores_per_game'] = 50
        session.save()

        response = self.client.get(self.url)

        self_user_data = UserData.objects.get(user=self.user)
        self.assertEqual(self_user_data.scores, 50)
        self.assertEqual(len(response.context['top3_users_data']), 3)
        self.assertGreaterEqual(len(response.context['other_users_data']), 1)

    def test_leaderboard_without_scores_in_session(self):
        """
        Test the LeaderboardView without any scores in the session.
        Ensures that the leaderboard renders correctly even when no new scores are added.
        """
        self.client.login(username='testuser', password='password')

        response = self.client.get(self.url)

        self_user_data = UserData.objects.get(user=self.user)
        self.assertEqual(self_user_data.scores, 0)
        self.assertEqual(len(response.context['top3_users_data']), 3)
        self.assertGreaterEqual(len(response.context['other_users_data']), 1)
