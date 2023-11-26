import os

from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import Client
from django.test import override_settings
from django.core.management import call_command


class AuthenticationViewTest(TestCase):
    """
    Test cases for user authentication views, including the login process.
    """

    def setUp(self):
        """
          Set up data for the authentication tests.
          This includes loading initial data and creating a test user.
          """
        call_command('loaddata', os.getcwd() + '/data/google-oauth-data.json', '--exclude=contenttypes')
        self.username = 'testuser'
        self.password = 'Shankung123456'
        self.email = "adsadsa@sddsa.com"
        self.user = User.objects.create_user(username=self.username, password=self.password, email=self.email)

    def test_login_view(self):
        """
        Test the login process with valid and invalid credentials.
        Verifies that a user is redirected upon successful login and stays on the page if the login fails.
        """
        client = Client()
        response = client.post(reverse('login'), {'username': self.username, 'password': self.password})
        self.assertEqual(response.status_code, 302)
        response = client.post(reverse('login'), {'username': self.username, 'password': 'incorrect'})
        self.assertEqual(response.status_code, 200)

    def test_login_view_template(self):
        """
        Test that the login view uses the correct template.
        """
        client = Client()
        response = client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')


@override_settings(AUTH_PASSWORD_VALIDATORS=[])
class UserRegistrationTest(TestCase):
    """
    Test cases for user registration functionality.
    """
    def test_user_registration(self):
        """
        Test the user registration process with valid data.
        Verifies that a new user is created and redirected appropriately.
        """
        response = self.client.post(reverse('signup'), {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'email': 'testuser@example.com',
            'firstname': 'John',
            'lastname': 'Doe',
        })
        self.assertEqual(response.status_code, 302)

        user_created = User.objects.filter(username='testuser').exists()
        self.assertTrue(user_created)

    def test_user_registration_fail(self):
        """
        Test the failure of user registration due to non-matching passwords.
        The form should be invalid and the response should render the same registration page
        with a 200 status code.
        """
        response = self.client.post(reverse('signup'), {
            'username': 'testuser',
            'password1': 'test1234',
            'password2': 'test123',  # not match
            'email': 'testuser@example.com',
            'firstname': 'John',
            'lastname': 'Doe',
        })
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'password2', "The two password fields didn’t match.")
        self.assertFalse(User.objects.filter(username='testuser').exists())


class UserLogoutTest(TestCase):
    """
    Test cases for user logout functionality.
    """
    def setUp(self):
        """
        Set up for testing the logout process.
        Creates a test user to be used in the logout tests.
        """
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_user_logout(self):
        """
        Test that a logged-in user can successfully log out.
        Verifies that the logout process redirects the user.
        """
        client = Client()
        client.login(username='testuser', password='testpassword')
        response = client.post(reverse('logout'))
        self.assertEqual(response.status_code, 302)
