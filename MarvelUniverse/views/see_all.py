from django.shortcuts import render
from django.views import View
from ..models import Character, Comic, Series


class AllCharactersView(View):
    template_name = 'MarvelUniverse/see_all/all_characters.html'

    def get(self, request):
        characters = Character.objects.all()

        context = {
            'characters': characters,
        }
        return render(request, self.template_name, context)


class AllComicsView(View):
    template_name = 'MarvelUniverse/see_all/all_comics.html'

    def get(self, request):
        comics = Comic.objects.all()

        context = {
            'comics': comics,
        }
        return render(request, self.template_name, context)
    

class AllSeriesView(View):
    template_name = 'MarvelUniverse/see_all/all_series.html'

    def get(self, request):
        series = Series.objects.all()

        context = {
            'series': series,
        }
        return render(request, self.template_name, context)
    