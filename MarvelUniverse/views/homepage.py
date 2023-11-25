from django.shortcuts import render
from django.views import View
from ..models import Character, Comic, Series


class HomePageView(View):
    """
    View for rendering the homepage, displaying lists of characters, comics, and series.

    Attributes:
    - template_name (str): The HTML template to be used for rendering.

    Methods:
    - get(request): Handles HTTP GET requests, retrieves data, and renders the homepage.

    """
    template_name = 'MarvelUniverse/homepage.html'

    def get(self, request):
        """
        Handles HTTP GET requests, retrieves data, and renders the homepage.

        Parameters:
        - request (HttpRequest): The HTTP GET request.

        Returns:
        - HttpResponse: Rendered homepage.

        """
        characters = Character.objects.all()
        comics = Comic.objects.all()
        series = Series.objects.all()

        context = {
            'characters': characters,
            'comics': comics,
            'series': series
        }
        return render(request, self.template_name, context)
