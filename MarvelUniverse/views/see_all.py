from django.shortcuts import render
from django.views import View
from ..models import Character, Comic, Series
from django.http import JsonResponse


class AllCharactersView(View):
    template_name = 'MarvelUniverse/see_all/all_characters.html'

    def get(self, request):
        characters = Character.objects.all()
        context = {
            'characters': characters,
            'character_count': characters.count(),
        }
        return render(request, self.template_name, context)


class CharacterSearchView(View):
    def get(self, request):
        """
        Get the name of character search from user then find the match name and display for user.
        """
        search_query = request.GET.get("search", "")
        characters = Character.objects.filter(name__icontains=search_query).values('name', 'image', 'id')
        return JsonResponse(list(characters), safe=False)


class AllComicsView(View):
    template_name = 'MarvelUniverse/see_all/all_comics.html'

    def get(self, request):
        comics = Comic.objects.all()
        context = {
            'comics': comics,
            'comics_count': comics.count(),
        }
        return render(request, self.template_name, context)


class ComicSearchView(View):
    """
    Get the title of comic search from user then find the match name and display for user.
    """
    def get(self, request):
        search_query = request.GET.get("search", "")
        comic = Comic.objects.filter(title__icontains=search_query).values('title', 'image', 'id')
        return JsonResponse(list(comic), safe=False)


class AllSeriesView(View):
    template_name = 'MarvelUniverse/see_all/all_series.html'

    def get(self, request):
        series = Series.objects.all()
        context = {
            'series': series,
            'series_count': series.count(),
        }
        return render(request, self.template_name, context)


class SeriesSearchView(View):
    """
    Get the title name of series search from user then find the match name and display for user.
    """
    def get(self, request):
        search_query = request.GET.get("search", "")
        series = Series.objects.filter(title__icontains=search_query).values("title", "image", "id")
        return JsonResponse(list(series), safe=False)
