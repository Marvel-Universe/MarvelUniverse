from django.urls import reverse
from django.shortcuts import render
from django.views import View
from django.contrib import messages
from django.http import HttpResponseRedirect
from ..forms import SeriesCommentForm, ComicCommentForm
from ..models.comment_models import SeriesComment, ComicComment
from ..models import Character, Comic, Series, CharacterInComic, CharacterInSeries


class CharactersDetailView(View):
    template_name = 'MarvelUniverse/detail/characters.html'

    def get(self, request, character_pk):
        try:
            character = Character.objects.get(pk=character_pk)
        except Character.DoesNotExist:
            messages.error(f"Character {character_pk} not found")
            return HttpResponseRedirect(reverse('MarvelUniverse:characters'))
        else:
            characters_comics = CharacterInComic.objects.filter(character=character)
            characters_series = CharacterInSeries.objects.filter(character=character)
        comics_list = [character_comic.comic for character_comic in characters_comics]
        series_list = [character_series.series for character_series in characters_series]
        context = {
            'character': character,
            'comics_list': comics_list,
            'series_list': series_list,
            'comics_count': characters_comics.count(),
            'series_count': characters_series.count(),
        }
        return render(request, self.template_name, context)   


def comic_detail_view(request, comic_pk):
    try:
        comic = Comic.objects.get(pk=comic_pk)
    except Comic.DoesNotExist:
        messages.error(f"Comic {comic_pk} not found")
        return HttpResponseRedirect(reverse('MarvelUniverse:comics'))
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
    context = {
        'comic': comic,
        'characters_list': characters_list,
        'characters_count': characters_series.count(),
        'comic_comments': comic_comments,
        'comic_comments_count': comic_comments.count(),
        'comment_form': comment_form,
    }
    return render(request, 'MarvelUniverse/detail/comics.html', context)


def series_detail_view(request, series_pk):
    try:
        series = Series.objects.get(pk=series_pk)
    except Series.DoesNotExist:
        messages.error(f"Series {series_pk} not found")
        return HttpResponseRedirect(reverse('MarvelUniverse:series'))
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
    context = {
        'series': series,
        'characters_list': characters_list,
        'characters_count': characters_series.count(),
        'series_comments': series_comments,
        'series_comments_count': series_comments.count(),
        'comment_form': comment_form
    }
    return render(request, 'MarvelUniverse/detail/series.html', context)
