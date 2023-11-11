from django.shortcuts import render
from django.views import View
from ..models import Character, Comic, Series, CharacterInComic, CharacterInSeries
from django.contrib import messages


class CharactersDetailView(View):
    template_name = 'MarvelUniverse/detail/characters.html'

    def get(self, request, character_pk):
        try:
            character = Character.objects.get(pk=character_pk)
        except Character.DoesNotExist:
            messages.error(f"Character {character_pk} not found")
        else:
            characters_comics = CharacterInComic.objects.filter(character=character)
            characters_series = CharacterInSeries.objects.filter(character=character)
        comics_list = [character_comic.comic for character_comic in characters_comics]
        series_list = [character_series.series for character_series in characters_series]
        context = {
            'character': character,
            'comics_list': comics_list,
            'series_list': series_list,
            'comics_count': characters_comics.count(),
            'series_count': characters_series.count()
        }
        return render(request, self.template_name, context)
    

class ComicsDetailView(View):
    template_name = 'MarvelUniverse/detail/comics.html'

    def get(self, request, comic_pk):
        try:
            comic = Comic.objects.get(pk=comic_pk)
        except Character.DoesNotExist:
            messages.error(f"Comic {comic_pk} not found")
        else:
            characters_comics = CharacterInComic.objects.filter(comic=comic)
        characters_list = [character_comic.character for character_comic in characters_comics]
        context = {
            'comic': comic,
            'characters_list': characters_list,
            'characters_count': characters_comics.count(),
        }
        return render(request, self.template_name, context)


class SeriesDetailView(View):
    template_name = 'MarvelUniverse/detail/series.html'

    def get(self, request, series_pk):
        try:
            series = Series.objects.get(pk=series_pk)
        except Character.DoesNotExist:
            messages.error(f"Comic {series_pk} not found")
        else:
            characters_series = CharacterInSeries.objects.filter(series=series)
        characters_list = [character_series.character for character_series in characters_series]
        context = {
            'series': series,
            'characters_list': characters_list,
            'characters_count': characters_series.count(),
        }
        return render(request, self.template_name, context)
    