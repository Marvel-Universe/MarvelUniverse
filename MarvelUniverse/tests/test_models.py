import os

from ..models.marvel_models import Character, Series, Comic, CharacterInSeries, CharacterInComic
from ..models.comment_models import SeriesComment, ComicComment, CharacterComment
from ..models.favorites import FavoriteCharacter, FavoriteComic, FavoriteSeries
from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.management import call_command


class CommentModelsTest(TestCase):
    def setUp(self):
        call_command('loaddata', os.getcwd() + '/data/google-oauth-data.json', '--exclude=contenttypes')
        self.user = User.objects.create_user(username='Sankung', password='Sankung1234')
        self.series = Series.objects.create(title='San series')
        self.comic = Comic.objects.create(title='San comic')
        self.character = Character.objects.create(name='San character')

        self.series_comment = SeriesComment.objects.create(
            series=self.series,
            user=self.user,
            user_comment='Nice series',
            created_on=timezone.now(),
            active=True
        )
        self.comic_comment = ComicComment.objects.create(
            comic=self.comic,
            user=self.user,
            user_comment='Nice comic',
            created_on=timezone.now(),
            active=True
        )

        self.character_comment = CharacterComment.objects.create(
            character=self.character,
            user=self.user,
            user_comment='Nice character',
            created_on=timezone.now(),
            active=True
        )

    def test_comment_created(self):
        self.assertEqual(self.series_comment.user_comment, 'Nice series')
        self.assertEqual(self.series_comment.user, self.user)
        self.assertTrue(self.series_comment.active)

        self.assertEqual(self.comic_comment.user_comment, 'Nice comic')
        self.assertEqual(self.comic_comment.user, self.user)
        self.assertTrue(self.comic_comment.active)

        self.assertEqual(self.character_comment.user_comment, 'Nice character')
        self.assertEqual(self.character_comment.user, self.user)
        self.assertTrue(self.character_comment.active)

    def test_ordering(self):
        latest_comment_series = SeriesComment.objects.latest('created_on')
        self.assertEqual(latest_comment_series, self.series_comment)

        latest_comment_comic = ComicComment.objects.latest('created_on')
        self.assertEqual(latest_comment_comic, self.comic_comment)

        latest_comment_character = ComicComment.objects.latest('created_on')
        self.assertEqual(latest_comment_character, self.comic_comment)


class FavoriteModelsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

        self.character = Character.objects.create(name='Spider-Man')
        self.comic = Comic.objects.create(title='Amazing Spider-Man #1')
        self.series = Series.objects.create(title='The Spider-Man Chronicles')

        self.favorite_character = FavoriteCharacter.objects.create(user=self.user, character=self.character)
        self.favorite_comic = FavoriteComic.objects.create(user=self.user, comic=self.comic)
        self.favorite_series = FavoriteSeries.objects.create(user=self.user, series=self.series)

    def test_favorites_linked_properly(self):
        self.assertEqual(self.favorite_character.user, self.user)
        self.assertEqual(self.favorite_character.character, self.character)

        self.assertEqual(self.favorite_comic.user, self.user)
        self.assertEqual(self.favorite_comic.comic, self.comic)

        self.assertEqual(self.favorite_series.user, self.user)
        self.assertEqual(self.favorite_series.series, self.series)

class MarvelModelsTest(TestCase):
    def setUp(self):
        # Create instances of Character, Comic, and Series
        self.character = Character.objects.create(name='Iron Man', description='A wealthy industrialist and genius inventor', image='http://image.url/ironman')
        self.comic = Comic.objects.create(title='Iron Man #1', description='The first issue of Iron Man', image='http://image.url/ironman1')
        self.series = Series.objects.create(title='The Iron Man Adventures', description='A series following the adventures of Iron Man', image='http://image.url/series/ironman')

        # Create instances for CharacterInComic and CharacterInSeries
        self.character_in_comic = CharacterInComic.objects.create(character=self.character, comic=self.comic)
        self.character_in_series = CharacterInSeries.objects.create(character=self.character, series=self.series)

    def test_character_str(self):
        self.assertEqual(str(self.character), 'Iron Man')

    def test_comic_str(self):
        self.assertEqual(str(self.comic), 'Iron Man #1')

    def test_series_str(self):
        self.assertEqual(str(self.series), 'The Iron Man Adventures')

    def test_character_in_comic_str(self):
        self.assertEqual(str(self.character_in_comic), 'Iron Man in Iron Man #1')

    def test_character_in_series_str(self):
        self.assertEqual(str(self.character_in_series), 'Iron Man in The Iron Man Adventures')

    def test_nullable_fields(self):
        # Test creating instances with null fields
        character_null = Character.objects.create()
        comic_null = Comic.objects.create()
        series_null = Series.objects.create()
        character_in_comic_null = CharacterInComic.objects.create()
        character_in_series_null = CharacterInSeries.objects.create()

        self.assertIsNone(character_null.name)
        self.assertIsNone(comic_null.title)
        self.assertIsNone(series_null.title)
        self.assertIsNone(character_in_comic_null.character)
        self.assertIsNone(character_in_comic_null.comic)
        self.assertIsNone(character_in_series_null.character)
        self.assertIsNone(character_in_series_null.series)
