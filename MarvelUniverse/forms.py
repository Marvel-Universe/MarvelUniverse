from .models.comment_models import SeriesComment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = SeriesComment
        fields = ['user_comment']
