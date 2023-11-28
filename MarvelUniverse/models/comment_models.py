from django.db import models
from .marvel_models import Series, Comic, Character
from django.contrib.auth.models import User


class SeriesComment(models.Model):
    """
    Model to represent comments on a Series.

    Attributes:
    - series (Series): The Series being commented on.
    - user (User): The user who made the comment.
    - user_comment (str): The content of the comment.
    - created_on (DateTime): The timestamp when the comment was created.
    - active (bool): A flag indicating whether the comment is active or not.

    """
    series = models.ForeignKey(Series, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='series_comments')
    user_comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        """
        - ordering: Orders comments based on their creation timestamp.
        """
        ordering = ['created_on']

    def __str__(self):
        """
        String representation of the SeriesComment object.

        Returns:
        str: A string representing the comment and its author.
        """
        return 'Comment {} by {}'.format(self.user_comment, self.user)


class ComicComment(models.Model):
    """
    Model to represent comments on a Comic.

    Attributes:
    - comic (Comic): The Comic being commented on.
    - user (User): The user who made the comment.
    - email (EmailField): Email of the user making the comment.
    - user_comment (str): The content of the comment.
    - created_on (DateTime): The timestamp when the comment was created.
    - active (bool): A flag indicating whether the comment is active or not.
    """
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comic_comments')
    email = models.EmailField(max_length=50)
    user_comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        """
        Meta:
        - ordering: Orders comments based on their creation timestamp.
        """
        ordering = ['created_on']

    def __str__(self):
        """
        String representation of the ComicComment object.

        Returns:
        str: A string representing the comment, its author, and the associated comic.
        """
        return 'Comment {} by {} on {}'.format(self.user_comment, self.user, self.comic)


class CharacterComment(models.Model):
    """
    Model to represent comments on a Character.

    Attributes:
    - character (Character): The Character being commented on.
    - user (User): The user who made the comment.
    - email (EmailField): Email of the user making the comment.
    - user_comment (str): The content of the comment.
    - created_on (DateTime): The timestamp when the comment was created.
    - active (bool): A flag indicating whether the comment is active or not.
    """
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='character_comments')
    email = models.EmailField(max_length=50)
    user_comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        """
        Meta:
        - ordering: Orders comments based on their creation timestamp.
        """
        ordering = ['created_on']

    def __str__(self):
        """
        String representation of the CharacterComment object.

        Returns:
        str: A string representing the comment, its author, and the associated character.
        """
        return 'Comment {} by {} on {}'.format(self.user_comment, self.user, self.character)
