import os
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Character, Comic, Series, CharacterComment, ComicComment, SeriesComment
from django.core.management import call_command


class CharacterDetailViewTest(TestCase):
    """
    Test suite for the character detail view functionality.
    """
    def setUp(self):
        """
        Set up for testing the character detail view.
        Includes loading test data, creating a test user, and a test character.
        """
        call_command('loaddata', os.getcwd() + '/data/google-oauth-data.json', '--exclude=contenttypes')
        self.client = Client()
        self.user = User.objects.create_user(username='Character test', email='character@gmail.com',
                                             password='character123')
        self.character = Character.objects.create(name='Test Character')
        self.detail_url = reverse('MarvelUniverse:characters-detail', kwargs={'character_pk': self.character.pk})

    def test_character_detail_get(self):
        """
         Test the GET request to the character detail page.
         Verifies that the response is 200 OK and the character's name is in the response.
        """
        self.client.force_login(self.user)
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.character.name)

    def test_character_detail_post_comment(self):
        """
        Test the POST request to the character detail page for comment submission.
        Verifies that submitting a valid comment creates a CharacterComment instance.
        """
        self.client.force_login(self.user)
        response = self.client.post(self.detail_url, {'user_comment': 'Great character!'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(CharacterComment.objects.filter(user=self.user, character=self.character).exists())


class ComicDetailViewTest(TestCase):
    """
    Test suite for the comic detail view functionality.
    """
    def setUp(self):
        """
        Set up for testing the comic detail view.
        Includes creating a test user and a test comic.
        """
        self.client = Client()
        self.user = User.objects.create_user(username='Comic test', email='comic@gmail.com', password='comic123')
        self.comic = Comic.objects.create(title='Test Comic')
        self.comic_url = reverse('MarvelUniverse:comics-detail', kwargs={'comic_pk': self.comic.pk})

    def test_comic_detail_get(self):
        """
        Test the GET request to the comic detail page.
        Verifies that the response is 200 OK and the comic's title is in the response.
        """
        self.client.force_login(self.user)
        response = self.client.get(self.comic_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.comic.title)

    def test_comic_detail_post_comment(self):
        """
        Test the POST request to the comic detail page for comment submission.
        Verifies that submitting a valid comment creates a ComicComment instance.
        """
        self.client.force_login(self.user)
        response = self.client.post(self.comic_url, {'user_comment': 'Greate comic'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(ComicComment.objects.filter(user=self.user, comic=self.comic).exists())


class SeriesDetailViewTest(TestCase):
    """
    Test suite for the series detail view functionality.
    """
    def setUp(self):
        """
        Set up for testing the series detail view.
        Includes creating a test user and a test series.
        """
        self.client = Client()
        self.user = User.objects.create_user(username='Series test', email='series@gmail.com', password='series123')
        self.series = Series.objects.create(title='Test Series')
        self.series_url = reverse('MarvelUniverse:series-detail', kwargs={'series_pk': self.series.pk})

    def test_series_detail_get(self):
        """
        Test the GET request to the series detail page.
        Verifies that the response is 200 OK and the series' title is in the response.
        """
        self.client.force_login(self.user)
        response = self.client.get(self.series_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.series.title)

    def test_comic_detail_post_comment(self):
        """
        Test the POST request to the series detail page for comment submission.
        Verifies that submitting a valid comment creates a SeriesComment instance.
        """
        self.client.force_login(self.user)
        response = self.client.post(self.series_url, {'user_comment': 'Greate series'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(SeriesComment.objects.filter(user=self.user, series=self.series).exists())
