from django.db import models
from .marvel_models import Series
from django.contrib.auth.models import User


class SeriesComment(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    user_comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.user_comment, self.user)
    