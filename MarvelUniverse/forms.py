from .models.comment_models import SeriesReview
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = SeriesReview
        fields = ('name', 'email', 'body')

    # series_slug = forms.CharField(widget=forms.HiddenInput())