from django.db import models
from django.contrib.auth.models import User


class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_data')
    profile_img_url = models.URLField(max_length=500, blank=True, null=True)  # get link from character
    scores = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username