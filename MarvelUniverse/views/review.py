# from django.shortcuts import render, get_object_or_404
# from ..models.marvel_models import Series
# from ..models.comment_models import SeriesReview  # Import the SeriesReview model
# from ..forms import CommentForm
#
#
# def series_detail(request):
#     template_name = 'MarvelUniverse/detail_all/series_detail.html'
#     series = Series.objects.first()
#     # comments = series.comments.filter(active=True)  # Fetch comments related to the series
#     comments = SeriesReview.objects.filter(series=series, active=True)
#
#
#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             new_comment = comment_form.save(commit=False)
#             new_comment.series = series
#             new_comment.active = True
#             new_comment.save()
#     else:
#         comment_form = CommentForm()
#
#     return render(request, template_name, {'series': series, 'comments': comments, 'comment_form': comment_form})

# def series_detail(request, slug):
#     template_name = 'MarvelUnivers/detail_all/series_detail.html'
#     series = get_object_or_404(Series, slug=slug)

#     # Retrieve all comments related to the specific series
#     comments = SeriesReview.objects.filter(series=series, active=True)

#     new_comment = None

#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             new_comment = comment_form.save(commit=False)
#             new_comment.series = series
#             new_comment.active = True
#             new_comment.save()
#     else:
#         comment_form = CommentForm(initial={'series_slug': series.slug})

#     return render(request, template_name, {'series': series, 'comments': comments, 'comment_form': comment_form})