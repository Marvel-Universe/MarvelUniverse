from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views import View
from ..models import Character, Comic, Series, FavoriteCharacter, FavoriteComic, FavoriteSeries
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin


class FavoriteView(LoginRequiredMixin,View):
    """
    View for displaying the user's favorite characters, comics, and series.

    Attributes:
    - template_name (str): The name of the template to be used for rendering the view.
    - login_url (str): The URL to redirect to if the user is not logged in.
    - redirect_field_name (str): The name of the redirect field value in the request.

    Methods:
    - get(self, request): Handles GET requests and renders the favorites template.

    """
    template_name = 'MarvelUniverse/favorites.html'
    login_url = 'login'
    redirect_field_name = 'login'

    def get(self, request):
        """
        Handle GET requests and render the favorites template.

        """
        favorite_character = FavoriteCharacter.objects.filter(user=request.user)
        favorite_comic = FavoriteComic.objects.filter(user=request.user)
        favorite_series = FavoriteSeries.objects.filter(user=request.user)
        characters_list = [favorite.character for favorite in favorite_character]
        comics_list = [favorite.comic for favorite in favorite_comic]
        series_list = [favorite.series for favorite in favorite_series]
        context = {
            'characters_list': characters_list,
            'comics_list': comics_list,
            'series_list': series_list,
            'characters_count': len(characters_list),
            'comics_count': len(comics_list),
            'series_count': len(series_list)
        }
        return render(request, self.template_name, context)


@login_required(login_url='login')
def toggle_favorite(request, model, object_id):
    """
    Toggle the favorite status of a character, comic, or series for the logged-in user.

    Args:
    - request (HttpRequest): The HTTP request object.
    - model (str): The type of the model (character, comic, or series).
    - object_id (int): The ID of the object to toggle the favorite status.

    Returns:
    - JsonResponse: A JSON response indicating whether the object is now a favorite.

    """
    user = request.user
    is_favorite = False

    model_class_map = {
        'character': (Character, FavoriteCharacter),
        'comic': (Comic, FavoriteComic),
        'series': (Series, FavoriteSeries),
    }

    model_class = model_class_map.get(model)
    if model_class:
        obj = model_class[0].objects.filter(pk=object_id).first()
        favorite_model = model_class[1]

        if obj:
            favorite_instance, created = favorite_model.objects.get_or_create(user=user, **{model: obj})
            if not created:
                favorite_instance.delete()
            else:
                is_favorite = True
        else:
            return JsonResponse({'error': 'Object not found'})
    else:
        return JsonResponse({'error': 'Invalid model type'})

    return JsonResponse({'is_favorite': is_favorite})
