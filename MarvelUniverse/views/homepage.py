from django.shortcuts import render
from django.views import View
from ..models import Character, Comic, Series


class HomePageView(View):
    template_name = 'MarvelUniverse/homepage.html'

    def get(self, request):
        characters = Character.objects.all()
        comics = Comic.objects.all()
        series = Series.objects.all()

        context = {
            'characters': characters,
            'comics': comics,
            'series': series
        }
        return render(request, self.template_name, context)
