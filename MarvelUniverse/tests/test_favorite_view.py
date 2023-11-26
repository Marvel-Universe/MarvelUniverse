import os

from django.contrib.auth.models import User
from django.urls import reverse
from ..models import Character, Comic, Series, FavoriteCharacter, FavoriteComic, FavoriteSeries
from django.core.management import call_command
from django.test import TestCase, Client


class FavoriteViewTest(TestCase):
    """
    Test suite for the FavoriteView, which shows the user's favorite characters, comics, and series.
    """
    def setUp(self):
        """
        Set up for testing the FavoriteView.
        Loads initial data, creates a test user, and favorite instances for character, comic, and series.
        """
        call_command('loaddata', os.getcwd() + '/data/google-oauth-data.json', '--exclude=contenttypes')
        self.client = Client()
        self.favorite_path = reverse('MarvelUniverse:favorites')
        self.user = User.objects.create_user(username='San teset', password='test1234')
        self.character = Character.objects.create(name='Spider-Man')
        self.comic = Comic.objects.create(title='Amazing Spider-Man #1')
        self.series = Series.objects.create(title='The Spider-Man Chronicles')
        self.favorite_character = FavoriteCharacter.objects.create(user=self.user, character=self.character)
        self.favorite_comic = FavoriteComic.objects.create(user=self.user, comic=self.comic)
        self.favorite_series = FavoriteSeries.objects.create(user=self.user, series=self.series)

    def test_favorite_view(self):
        """
        Test the GET request to the favorite page.
        Verifies that the response is 200 OK and the context contains the lists of favorite characters, comics, and series.
        """
        self.client.force_login(self.user)
        response = self.client.get(self.favorite_path)

        self.assertEqual(response.status_code, 200)
        self.assertIn('characters_list', response.context)
        self.assertIn('comics_list', response.context)
        self.assertIn('series_list', response.context)
        self.assertIn(self.character, response.context['characters_list'])
        self.assertIn(self.comic, response.context['comics_list'])
        self.assertIn(self.series, response.context['series_list'])


class ToggleFavoriteTest(TestCase):
    """
    Test suite for the functionality to toggle an item (character, comic, or series) as a favorite.
    """
    def setUp(self):
        """
        Set up for testing the toggle favorite functionality.
        Creates a test user and instances for character, comic, and series.
        """
        self.client = Client()
        self.user = User.objects.create_user(username='Oattest', password='oat123')
        self.character = Character.objects.create(name='Spider-Man')
        self.comic = Comic.objects.create(title='Amazing Spider-Man #1')
        self.series = Series.objects.create(title='The Spider-Man Chronicles')

        self.client.force_login(self.user)

    def test_toggle_favorite_character(self):
        """
        Test the toggle functionality for a favorite character.
        Verifies that the character can be added and removed from the user's favorites.
        """
        toggle_url = reverse('MarvelUniverse:toggle_favorite', args=['character', self.character.id])
        response = self.client.post(toggle_url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['is_favorite'])
        self.assertTrue(FavoriteCharacter.objects.filter(user=self.user, character=self.character).exists())
        response = self.client.post(toggle_url)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.json()['is_favorite'])
        self.assertFalse(FavoriteCharacter.objects.filter(user=self.user, character=self.character).exists())

