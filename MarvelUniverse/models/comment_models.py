from django.db import models
from .marvel_models import Series, Comic
from django.contrib.auth.models import User


class SeriesComment(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='series_comments')
    user_comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.user_comment, self.user)


class ComicComment(models.Model):
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comic_comments')
    email = models.EmailField(max_length=50)
    user_comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {} on {}'.format(self.user_comment, self.user, self.comic)
    