from django.test import TestCase, Client
from django.urls import reverse
from ..models import Character, Comic, Series
import json

class AllViewsTest(TestCase):
    """
    Test suite for views displaying all characters, comics, and series,
    and their corresponding search views.
    """

    def setUp(self):
        """
        Set up data for testing views.
        This includes creating test instances for Character, Comic, and Series.
        """
        self.client = Client()
        Character.objects.create(name='Spider-Man', image='spiderman_image_url')
        Comic.objects.create(title='Amazing Spider-Man #1', image='spiderman_comic_image_url')
        Series.objects.create(title='The Spider-Man Chronicles', image='spiderman_series_image_url')

    def test_all_characters_view(self):
        """
        Test the AllCharactersView for correct rendering and context data.
        """
        response = self.client.get(reverse('MarvelUniverse:characters'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['characters']), Character.objects.count())

    def test_character_search_view(self):
        """
        Test the CharacterSearchView for correct JSON response and search functionality.
        """
        response = self.client.get(reverse('MarvelUniverse:character_search'), {'search': 'Spider'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['count'], 1)
        self.assertEqual(data['characters'][0]['name'], 'Spider-Man')

    def test_all_comics_view(self):
        """
        Test the AllComicsView for correct rendering and context data.
        """
        response = self.client.get(reverse('MarvelUniverse:comics'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['comics']), Comic.objects.count())

    def test_comic_search_view(self):
        """
        Test the ComicSearchView for correct JSON response and search functionality.
        """
        response = self.client.get(reverse('MarvelUniverse:comic_search'), {'search': 'Spider'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['count'], 1)
        self.assertEqual(data['comics'][0]['title'], 'Amazing Spider-Man #1')

    def test_all_series_view(self):
        """
        Test the AllSeriesView for correct rendering and context data.
        """
        response = self.client.get(reverse('MarvelUniverse:series'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['series']), Series.objects.count())

    def test_series_search_view(self):
        """
        Test the SeriesSearchView for correct JSON response and search functionality.
        """
        response = self.client.get(reverse('MarvelUniverse:series_search'), {'search': 'Spider'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['count'], 1)
        self.assertEqual(data['series'][0]['title'], 'The Spider-Man Chronicles')