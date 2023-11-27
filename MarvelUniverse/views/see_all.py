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
        characters = Character.objects.filter(name__icontains=search_query)
        data = {
            'characters': list(characters.values('name', 'image', 'id')),
            'count': characters.count()
        }
        return JsonResponse(data)


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
        comics = Comic.objects.filter(title__icontains=search_query)
        data = {
            "comics": list(comics.values('title', 'image', 'id')),
            "count": comics.count()
        }
        return JsonResponse(data)


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
        series = Series.objects.filter(title__icontains=search_query)
        data = {
            "series": list(series.values('title', 'image', 'id')),
            "count": series.count()
        }
        return JsonResponse(data)
