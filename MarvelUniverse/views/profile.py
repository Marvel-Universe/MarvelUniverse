from django.views import View
from django.shortcuts import render


class ProfileView(View):
    """
    View for rendering the user profile page.

    Attributes:
    - template_name (str): The path to the HTML template used for rendering the profile page.

    Methods:
    - get(request): Handles HTTP GET requests to display the user's profile page.

    Usage:
    1. Create an instance of this view and include it in your URL patterns.
    2. Customize the 'MarvelUniverse/profile.html' template to display user-specific information.
    """
    template_name = 'MarvelUniverse/profile.html'

    def get(self, request):
        """
        Handle GET requests to render the user's profile page.

        Args:
        - request (HttpRequest): The HTTP request object.

        Returns:
        - HttpResponse: The rendered profile page.
        """
        return render(request, self.template_name)
