from ..models import Character, Comic, Series, CharacterInComic, CharacterInSeries
from django.contrib import messages
from django.shortcuts import render
from ..forms import SeriesCommentForm, ComicCommentForm, CharacterCommentForm
from ..models.comment_models import SeriesComment, ComicComment, CharacterComment
from ..models import FavoriteCharacter, FavoriteComic, FavoriteSeries
from django.http import HttpResponseRedirect
from django.urls import reverse


def character_detail_view(request, character_pk):
    """
    View to display details about a character, including associated comics, series, and user comments.

    Parameters:
    - request (HttpRequest): The HTTP request.
    - character_pk (int): The primary key of the character.

    Returns:
    - HttpResponse: Rendered character details page.

    """
    try:
        character = Character.objects.get(pk=character_pk)
    except Character.DoesNotExist:
        messages.error(f"Character {character_pk} not found")
        return HttpResponseRedirect(reverse('MarvelUniverse:all-characters'))
    else:
        characters_comics = CharacterInComic.objects.filter(character=character)
        characters_series = CharacterInSeries.objects.filter(character=character)
    comics_list = [character_comic.comic for character_comic in characters_comics]
    series_list = [character_series.series for character_series in characters_series]
    if request.method == 'GET':
        initial_data = {'user_comment': ''}
        comment_form = CharacterCommentForm(initial=initial_data)
    elif request.method == 'POST':
        comment_form = CharacterCommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.character = character
            new_comment.user = request.user
            new_comment.active = True
            new_comment.save()
            initial_data = {'user_comment': ''}
            comment_form = CharacterCommentForm(initial=initial_data)
    character_comments = CharacterComment.objects.filter(character=character, active=True)
    if request.user.is_authenticated:
        is_favorite = FavoriteCharacter.objects.filter(user=request.user, character=character).exists()
    else:
        is_favorite = False
    context = {
        'character': character,
        'comics_list': comics_list,
        'series_list': series_list,
        'comics_count': characters_comics.count(),
        'series_count': characters_series.count(),
        'is_favorite': is_favorite,
        'character_comments': character_comments,
        'comment_form': comment_form,
        'character_comments_count': character_comments.count(),
    }
    return render(request, 'MarvelUniverse/detail/characters.html', context)


# @login_required(login_url='login')
def comic_detail_view(request, comic_pk):
    """
     View to display details about a comic, including associated characters, user comments, and favorite status.

     Parameters:
     - request (HttpRequest): The HTTP request.
     - comic_pk (int): The primary key of the comic.

     Returns:
     - HttpResponse: Rendered comic details page.

     """
    try:
        comic = Comic.objects.get(pk=comic_pk)
    except Comic.DoesNotExist:
        messages.error(f"Comic {comic_pk} not found")
        return HttpResponseRedirect(reverse('MarvelUniverse:all-comics'))
    else:
        characters_series = CharacterInComic.objects.filter(comic=comic)
        characters_list = [character_series.character for character_series in characters_series]
    if request.method == 'GET':
        initial_data = {'user_comment': ''}
        comment_form = ComicCommentForm(initial=initial_data)
    elif request.method == 'POST':
        comment_form = ComicCommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.comic = comic
            new_comment.user = request.user
            new_comment.active = True
            new_comment.save()
            initial_data = {'user_comment': ''}
            comment_form = ComicCommentForm(initial=initial_data)
    comic_comments = ComicComment.objects.filter(comic=comic, active=True)
    if request.user.is_authenticated:
        is_favorite = FavoriteComic.objects.filter(user=request.user, comic=comic).exists()
    else:
        is_favorite = False
    context = {
        'comic': comic,
        'characters_list': characters_list,
        'characters_count': characters_series.count(),
        'comic_comments': comic_comments,
        'comic_comments_count': comic_comments.count(),
        'comment_form': comment_form,
        'is_favorite': is_favorite
    }
    return render(request, 'MarvelUniverse/detail/comics.html', context)


# @login_required(login_url='login')
def series_detail_view(request, series_pk):
    """
    View to display details about a series, including associated characters, user comments, and favorite status.

    Parameters:
    - request (HttpRequest): The HTTP request.
    - series_pk (int): The primary key of the series.

    Returns:
    - HttpResponse: Rendered series details page.

    """
    try:
        series = Series.objects.get(pk=series_pk)
    except Series.DoesNotExist:
        messages.error(f"Series {series_pk} not found")
        return HttpResponseRedirect(reverse('MarvelUniverse:all-series'))
    else:
        characters_series = CharacterInSeries.objects.filter(series=series)
        characters_list = [character_series.character for character_series in characters_series]
    if request.method == 'GET':
        initial_data = {'user_comment': ''}
        comment_form = SeriesCommentForm(initial=initial_data)
    elif request.method == 'POST':
        comment_form = SeriesCommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.cleaned_data
            new_comment = comment_form.save(commit=False)
            new_comment.series = series
            new_comment.user = request.user
            new_comment.active = True
            new_comment.save()
            initial_data = {'user_comment': ''}
            comment_form = SeriesCommentForm(initial=initial_data)
    series_comments = SeriesComment.objects.filter(series=series, active=True)
    if request.user.is_authenticated:
        is_favorite = FavoriteSeries.objects.filter(user=request.user, series=series).exists()
    else:
        is_favorite = False
    context = {
        'series': series,
        'characters_list': characters_list,
        'characters_count': characters_series.count(),
        'series_comments': series_comments,
        'series_comments_count': series_comments.count(),
        'comment_form': comment_form,
        'is_favorite': is_favorite
    }
    return render(request, 'MarvelUniverse/detail/series.html', context)
