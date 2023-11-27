import os
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Character, Comic, Series
from django.core.management import call_command


class AllViewsTest(TestCase):
    """
    Test suite for the views displaying all characters, comics, and series.
    Includes tests for both default views and filtered search functionality.
    """

    def setUp(self):
        """
        Set up data for testing views.
        This includes creating test instances for Character, Comic, and Series.
        """
        call_command('loaddata', os.getcwd() + '/data/google-oauth-data.json', '--exclude=contenttypes')
        self.client = Client()
        Character.objects.create(name='Spider-Man')
        Comic.objects.create(title='Amazing Spider-Man #1')
        Series.objects.create(title='The Spider-Man Chronicles')
        self.character_all_url = reverse('MarvelUniverse:characters')
        self.comic_all_url = reverse('MarvelUniverse:comics')
        self.series_all_url = reverse('MarvelUniverse:series')

    def test_all_characters_view(self):
        """
        Test the AllCharactersView with and without a search query.
        Verifies correct retrieval and filtering of character data.
        """
        response = self.client.get(self.character_all_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['characters']), Character.objects.count())

        response = self.client.get(self.character_all_url, {'get_search': 'Spider'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['characters']), 1)
        self.assertEqual(response.context['get_search'], 'Spider')

    def test_all_comics_view(self):
        """
        Test the AllComicsView with and without a search query.
        Verifies correct retrieval and filtering of comic data.
        """
        response = self.client.get(self.comic_all_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['comics']), Comic.objects.count())

        response = self.client.get(self.comic_all_url, {'get_search': 'Spider'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['comics']), 1)
        self.assertEqual(response.context['get_search'], 'Spider')

    def test_all_series_view(self):
        """
        Test the AllSeriesView with and without a search query.
        Verifies correct retrieval and filtering of series data.
        """
        response = self.client.get(self.series_all_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['series']), Series.objects.count())

        response = self.client.get(self.series_all_url, {'get_search': 'Spider'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['series']), 1)
        self.assertEqual(response.context['get_search'], 'Spider')
