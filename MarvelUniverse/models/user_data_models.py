from django.db import models
from django.contrib.auth.models import User


class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_data')
    profile_img_url = models.URLField(max_length=500, blank=True, null=True)
    trophy_img = models.CharField(max_length=100, blank=True, null=True, default="")
    scores = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    @property
    def trophy_img_display(self):
        return self.trophy_img

    def ranking_scores(self):
        if 500 <= self.scores < 1000:
            self.trophy_img = "bronze trophy"
        elif 1000 <= self.scores < 2500:
            self.trophy_img = "silver trophy"
        elif self.scores >= 2500:
            self.trophy_img = "gold trophy"
        else:
            self.__trophy_img = ""
        self.save()
