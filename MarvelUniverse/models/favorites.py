from ..models import Character, Series, Comic
from django.db import models
from django.contrib.auth.models import User


class FavoriteCharacter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.username}'s favorite character"


class FavoriteComic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.username}'s favorite comic"


class FavoriteSeries(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.username}'s favorite series"
    