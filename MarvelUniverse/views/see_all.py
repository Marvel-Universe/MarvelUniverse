from django.shortcuts import render
from django.views import View
from ..models import Character, Comic, Series
from django.contrib import messages


class SeeAllCharactersView(View):
    template_name = 'MarvelUniverse/see_all/characters.html'

    def get(self, request):
        if "get_search" in request.GET:
            get_search = request.GET["get_search"]
            characters = Character.objects.filter(name__icontains=get_search)[:]

        else:
            characters = Character.objects.all()

        context = {
            'characters': characters,
        }
        return render(request, self.template_name, context)


class SeeAllComicsView(View):
    template_name = 'MarvelUniverse/see_all/comics.html'

    def get(self, request):
        if "get_search" in request.GET:
            get_search = request.GET["get_search"]
            comics = Comic.objects.filter(title__icontains=get_search)[:]
        else:
            comics = Comic.objects.all()

        context = {
            'comics': comics,
        }
        return render(request, self.template_name, context)
    

class SeeAllSeriesView(View):
    template_name = 'MarvelUniverse/see_all/series.html'

    def get(self, request):
        if "get_search" in request.GET:
            get_search = request.GET["get_search"]
            series = Series.objects.filter(title__icontains=get_search)[:]
        else:
            series = Series.objects.all()

        context = {
            'series': series,
        }
        return render(request, self.template_name, context)
    