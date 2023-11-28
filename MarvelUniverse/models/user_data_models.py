from django.db import models
from django.contrib.auth.models import User

class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_data')
    profile_img_url = models.URLField(max_length=500, blank=True, null=True, default="https://i.ibb.co/t8GgdVp/default-profile.png")
    medal_img = models.CharField(max_length=100, blank=True, null=True, default="")
    scores = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    @property
    def get_trophy_img(self):
        return self.medal_img

    def save(self, *args, **kwargs):
        self.medal_img = self.ranking_scores() 
        super().save(*args, **kwargs)

    def ranking_scores(self):
        if 500 <= self.scores < 1000:
            return "https://i.ibb.co/C8D4SXz/bronze-medal.png"
        elif 1000 <= self.scores < 2500:
            return "https://i.ibb.co/pzhdfsp/silver-medal.png"
        elif self.scores >= 2500:
            return "https://i.ibb.co/kJ173Hq/gold-medal.png"
        else:
            return ""
