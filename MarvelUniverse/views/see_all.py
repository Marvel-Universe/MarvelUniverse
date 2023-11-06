from django.shortcuts import render
from django.views import View
from ..models import Character, Comic, Series


class SeeAllCharactersView(View):
    template_name = 'MarvelUniverse/see_all/characters.html'

    def get(self, request):
        characters = Character.objects.all()

        context = {
            'characters': characters,
        }
        return render(request, self.template_name, context)


class SeeAllComicsView(View):
    template_name = 'MarvelUniverse/see_all/comics.html'

    def get(self, request):
        comics = Comic.objects.all()

        context = {
            'comics': comics,
        }
        return render(request, self.template_name, context)
    

class SeeAllSeriesView(View):
    template_name = 'MarvelUniverse/see_all/series.html'

    def get(self, request):
        series = Series.objects.all()

        context = {
            'series': series,
        }
        return render(request, self.template_name, context)
    