from ..models import Character, Series, Comic
from django.db import models
from django.contrib.auth.models import User


class FavoriteCharacter(models.Model):
    """
    Model to represent a user's favorite character.

    Attributes:
    - user (User): The user who marked the character as a favorite.
    - character (Character): The favorite character associated with the user.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)

    def __str__(self) -> str:
        """
        Methods:
        - __str__(): Returns a string representation of the favorite character, including the username.

        """
        return f"{self.user.username}'s favorite character"


class FavoriteComic(models.Model):
    """
    Model to represent a user's favorite comic.

    Attributes:
    - user (User): The user who marked the comic as a favorite.
    - comic (Comic): The favorite comic associated with the user.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)

    def __str__(self) -> str:
        """
         Methods:
        - __str__(): Returns a string representation of the favorite comic, including the username.

        """
        return f"{self.user.username}'s favorite comic"


class FavoriteSeries(models.Model):
    """
    Model to represent a user's favorite series.

    Attributes:
    - user (User): The user who marked the series as a favorite.
    - series (Series): The favorite series associated with the user.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)

    def __str__(self) -> str:
        """
        - __str__(): Returns a string representation of the favorite series, including the username.

        """
        return f"{self.user.username}'s favorite series"
