from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import Client
from django.test import override_settings


class AuthenticationViewTest(TestCase):
    """
    Test case for authentication views, including login.

    Methods:
    - setUp(self): Initialize test data and create a user for testing.
    - test_login_view(self): Test the login view with valid and invalid credentials.
    - test_login_view_template(self): Test the login view template.

    """
    def setUp(self):
        """
        Initialize test data and create a user for testing.
        """
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_view(self):
        """
        Test the login view with valid and invalid credentials.
        """
        client = Client()

        # Test when a user enters valid login credentials
        response = client.post(reverse('login'), {'username': self.username, 'password': self.password})
        self.assertEqual(response.status_code, 302)

        response = client.post(reverse('login'), {'username': self.username, 'password': 'incorrect'})
        self.assertEqual(response.status_code, 200)

    def test_login_view_template(self):
        """
        Test the login view template.
        """
        client = Client()
        response = client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')


@override_settings(AUTH_PASSWORD_VALIDATORS=[])
class UserRegistrationTest(TestCase):
    """
    Test case for user registration view.

    Methods:
    - test_user_registration(self): Test user registration with valid data.

    """
    def test_user_registration(self):
        """
        Test user registration with valid data.
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


class UserLogoutTest(TestCase):
    """
    Test case for user logout view.

    Methods:
    - setUp(self): Initialize test data and create a user for testing.
    - test_user_logout(self): Test user logout functionality.

    """
    def setUp(self):
        """
        Initialize test data and create a user for testing.
        """
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_user_logout(self):
        """
        Test user logout functionality.
        """
        client = Client()
        client.login(username='testuser', password='testpassword')
        response = client.post(reverse('logout'))
        self.assertEqual(response.status_code, 302)
