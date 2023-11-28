from django.views import View
from django.shortcuts import render


class AboutUsView(View):
    """
    View to display the 'About Us' page.

    Attributes:
    - template_name (str): The name of the template to be rendered.

    Methods:
    - get(request): Handles GET requests and renders the 'About Us' page.

    """
    template_name = 'MarvelUniverse/about.html'

    def get(self, request):
        """
        Handles GET requests and renders the 'About Us' page.

        Parameters:
        - request (HttpRequest): The HTTP GET request.

        Returns:
        - HttpResponse: Rendered 'About Us' page.

        """
        return render(request, self.template_name)
