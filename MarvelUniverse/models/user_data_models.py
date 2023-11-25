from django.db import models
from django.contrib.auth.models import User


class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_data')
    profile_img_url = models.URLField(max_length=500, blank=True, null=True, default="")
    trophy_img = models.URLField(max_length=100, blank=True, null=True, default="")
    scores = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    @property
    def trophy_img_display(self):
        return self.trophy_img

    def ranking_scores(self):
        if 500 <= self.scores < 1000:
            self.trophy_img = "https://i.ibb.co/C8D4SXz/bronze-medal.png"
        elif 1000 <= self.scores < 2500:
            self.trophy_img = "https://i.ibb.co/pzhdfsp/sliver-medal.png"
        elif self.scores >= 2500:
            self.trophy_img = "https://i.ibb.co/kJ173Hq/gold-medal.png"
        else:
            self.__trophy_img = ""
        self.save()
