import os
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from ..views.favorites import FavoriteView
from ..models import Character, Comic, Series, FavoriteCharacter, FavoriteComic, FavoriteSeries
from django.core.management import call_command
from django.urls import clear_url_caches

from django.test import Client


class FavoriteViewTest(TestCase):
    def setUp(self):
        call_command('loaddata', os.getcwd() + '/data/google-oauth-data.json', '--exclude=contenttypes')
        self.client = Client()
        self.favorite_path = reverse('MarvelUniverse:favorites')
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.character = Character.objects.create(name='Spider-Man')
        self.comic = Comic.objects.create(title='Amazing Spider-Man #1')
        self.series = Series.objects.create(title='The Spider-Man Chronicles')
        self.favorite_character = FavoriteCharacter.objects.create(user=self.user, character=self.character)
        self.favorite_comic = FavoriteComic.objects.create(user=self.user, comic=self.comic)
        self.favorite_series = FavoriteSeries.objects.create(user=self.user, series=self.series)

    def test_favorite_view(self):
        self.client.force_login(self.user)
        response = self.client.get(self.favorite_path)

        self.assertEqual(response.status_code, 200)
        self.assertIn('characters_list', response.context)
        self.assertIn('comics_list', response.context)
        self.assertIn('series_list', response.context)
        self.assertIn(self.character, response.context['characters_list'])
        self.assertIn(self.comic, response.context['comics_list'])
        self.assertIn(self.series, response.context['series_list'])

