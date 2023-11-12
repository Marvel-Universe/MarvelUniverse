from django.shortcuts import render
from django.views import View
from ..models import Character, Comic, Series, CharacterInComic, CharacterInSeries
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from ..forms import SeriesCommentForm, ComicCommentForm
from ..models.comment_models import SeriesComment, ComicComment
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView


class CharactersDetailView(View):
    template_name = 'MarvelUniverse/detail/characters.html'

    def get(self, request, character_pk):
        try:
            character = Character.objects.get(pk=character_pk)
        except Character.DoesNotExist:
            messages.error(f"Character {character_pk} not found")
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
            'series_count': characters_series.count()
        }
        return render(request, self.template_name, context)


class ComicsDetailView(View):
    template_name = 'MarvelUniverse/detail/comics.html'

    def get(self, request, comic_pk):
        try:
            comic = Comic.objects.get(pk=comic_pk)
        except Comic.DoesNotExist:
            messages.error(f"Comic {comic_pk} not found")
        else:
            characters_comics = CharacterInComic.objects.filter(comic=comic)
        characters_list = [character_comic.character for character_comic in characters_comics]
        context = {
            'comic': comic,
            'characters_list': characters_list,
            'characters_count': characters_comics.count(),
        }
        return render(request, self.template_name, context)


@login_required(login_url='login')
def series_detail_view(request, series_pk):
    if request.method == 'GET':
        try:
            series = Series.objects.get(pk=series_pk)
        except Series.DoesNotExist:
            messages.error(f"Series {series_pk} not found")
        else:
            characters_series = CharacterInSeries.objects.filter(series=series)
            characters_list = [character_series.character for character_series in characters_series]
        initial_data = {'user_comment': ''}
        comment_form = SeriesCommentForm(initial=initial_data)
        context = {
            'series': series,
            'characters_list': characters_list,
            'characters_count': characters_series.count(),
            'series_comments': SeriesComment.objects.filter(series=series),
            'comment_form': comment_form
        }
        return render(request, 'MarvelUniverse/detail/series.html', context)
    if request.method == 'POST':
        try:
            series = Series.objects.get(pk=series_pk)
        except Series.DoesNotExist:
            messages.error(f"Series {series_pk} not found")
        else:
            characters_series = CharacterInSeries.objects.filter(series=series)
            characters_list = [character_series.character for character_series in characters_series]
        comment_form = SeriesCommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.series = series
            new_comment.user = request.user
            print(request.user)
            new_comment.active = True
            new_comment.save()
            initial_data = {'user_comment': ''}
            comment_form = SeriesCommentForm(initial=initial_data)
    else:
        initial_data = {'user_comment': ''}
        comment_form = SeriesCommentForm(initial=initial_data)
    context = {
        'series': series,
        'characters_list': characters_list,
        'characters_count': characters_series.count(),
        'series_comments': SeriesComment.objects.filter(series=series),
        'comment_form': comment_form
    }
    return render(request, 'MarvelUniverse/detail/series.html', context)


@login_required(login_url='login')
def comic_detail_view(request, series_pk):  # series_pk
    template_name = 'MarvelUniverse/detail/comics.html'
    comic = get_object_or_404(Series, pk=series_pk)  # use when link with detail when have series_pk
    comments = ComicComment.objects.filter(comic=comic, active=True)

    if request.method == 'POST':
        comment_form = ComicCommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.comic = comic
            new_comment.active = True
            new_comment.user = request.user
            new_comment.save()
    else:
        initial_data = {'user_comment': ''}
        comment_form = ComicCommentForm(initial=initial_data)

    return render(request, template_name, {'comic': comic, 'comments': comments, 'comment_form': comment_form})
