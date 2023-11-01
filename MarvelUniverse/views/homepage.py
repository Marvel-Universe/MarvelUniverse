from django.shortcuts import render
from django.views import View
from ..models import Character, Comic, Series


class HomePageView(View):
    template_name = 'homepage.html'

    def get(self, request):
        characters = Character.objects.all()[:16]
        comics = Comic.objects.all()[:16]
        series = Series.objects.all()[:16]

        context = {
            'characters': characters,
            'comics': comics,
            'series': series
        }
        return render(request, self.template_name, context)
