from .models.comment_models import SeriesComment, ComicComment, CharacterComment
from django import forms


class SeriesCommentForm(forms.ModelForm):
    """
    Form for adding a comment to a Series.

    Fields:
    - user_comment (str): The content of the comment.

    """
    class Meta:
        model = SeriesComment
        fields = ['user_comment']


class ComicCommentForm(forms.ModelForm):
    """
    Form for adding a comment to a Comic.

    Fields:
    - user_comment (str): The content of the comment.

    """
    class Meta:
        model = ComicComment
        fields = ['user_comment']


class CharacterCommentForm(forms.ModelForm):
    """
    Form for adding a comment to a Character.

    Fields:
    - user_comment (str): The content of the comment.

    """
    class Meta:
        model = CharacterComment
        fields = ['user_comment']
