from django.shortcuts import render
from django.views import View
from ..models import Character, Comic, Series
from django.contrib import messages


class AllCharactersView(View):
    template_name = 'MarvelUniverse/see_all/all_characters.html'

    def get(self, request):
        search_value = request.GET.get("get_search", "")

        if search_value:
            characters = Character.objects.filter(name__icontains=search_value)
        else:
            characters = Character.objects.all()

        context = {
            'characters': characters,
            'character_count': characters.count(),
            'get_search': search_value,
        }
        return render(request, self.template_name, context)


class AllComicsView(View):
    template_name = 'MarvelUniverse/see_all/all_comics.html'

    def get(self, request):
        search_value = request.GET.get("get_search", "")
        if search_value:
            comics = Comic.objects.filter(title__icontains=search_value)[:]
        else:
            comics = Comic.objects.all()

        context = {
            'comics': comics,
            'comics_count': comics.count(),
            'get_search': search_value,
        }
        return render(request, self.template_name, context)


class AllSeriesView(View):
    template_name = 'MarvelUniverse/see_all/all_series.html'

    def get(self, request):
        search_value = request.GET.get("get_search", "")
        if search_value:
            series = Series.objects.filter(title__icontains=search_value)[:]
        else:
            series = Series.objects.all()

        context = {
            'series': series,
            'series_count': series.count(),
            'get_search': search_value,
        }
        return render(request, self.template_name, context)
