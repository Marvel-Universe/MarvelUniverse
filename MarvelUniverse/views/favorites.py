from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from MarvelUniverse.models import Character, Comic, Series, FavoriteCharacter, FavoriteComic, FavoriteSeries

from django.contrib.auth.decorators import user_passes_test


@login_required(login_url='login')
def toggle_favorite(request, model, object_id):
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
