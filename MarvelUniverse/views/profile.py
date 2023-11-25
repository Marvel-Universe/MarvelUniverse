from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.humanize.templatetags.humanize import naturaltime

from MarvelUniverse.models import UserData


class ProfileView(View):
    """
    View for rendering the user profile page.

    Attributes:
    - template_name (str): The path to the HTML template used for rendering the profile page.

    Methods:
    - get(request, username): Handles HTTP GET requests to display the user's profile page.

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
        - username (str): The username of the user.

        Returns:
        - HttpResponse or JsonResponse: The rendered profile page or JSON response.
        """
        # Get the user object based on the provided username
        this_user = request.user
        user_data, created = UserData.objects.get_or_create(user=this_user)

        formatted_date_joined = naturaltime(this_user.date_joined)

        context = {
            'username': this_user.username,
            'email': this_user.email,
            'profile_img_url': user_data.profile_img_url,
            'trophy_img': user_data.trophy_img,
            'scores': user_data.scores,
            'date_joined': formatted_date_joined,
        }

        return render(request, self.template_name, context=context)
