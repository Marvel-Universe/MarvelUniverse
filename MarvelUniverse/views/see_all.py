from django.shortcuts import render
from django.views import View
from ..models import Character, Comic, Series
from django.contrib import messages


class AllCharactersView(View):
    template_name = 'MarvelUniverse/see_all/all_characters.html'

    def get(self, request):
        if "get_search" in request.GET:
            get_search = request.GET["get_search"]
            characters = Character.objects.filter(name__icontains=get_search)[:]

        else:
            characters = Character.objects.all()

        context = {
            'characters': characters,
            'character_count': characters.count(),
            'get_search': request.GET["get_search"]
        }
        return render(request, self.template_name, context)


class AllComicsView(View):
    template_name = 'MarvelUniverse/see_all/all_comics.html'

    def get(self, request):
        if "get_search" in request.GET:
            get_search = request.GET["get_search"]
            comics = Comic.objects.filter(title__icontains=get_search)[:]
        else:
            comics = Comic.objects.all()

        context = {
            'comics': comics,
            'comics_count': comics.count()
        }
        return render(request, self.template_name, context)
    

class AllSeriesView(View):
    template_name = 'MarvelUniverse/see_all/all_series.html'

    def get(self, request):
        if "get_search" in request.GET:
            get_search = request.GET["get_search"]
            series = Series.objects.filter(title__icontains=get_search)[:]
        else:
            series = Series.objects.all()

        context = {
            'series': series,
            'series_count': series.count()
        }
        return render(request, self.template_name, context)
    