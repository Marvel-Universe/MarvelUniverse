from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=1000, null=True)
    image = models.URLField(null=True)

    def __str__(self) -> str:
        return self.name


class Comic(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=500, null=True)
    image = models.URLField(null=True)

    def __str__(self) -> str:
        return self.title


class Series(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=500, null=True)
    image = models.URLField(null=True)

    def __str__(self) -> str:
        return self.title


class CharacterInComic(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, null=True)
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.character.name + " in " + self.comic.title


class CharacterInSeries(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, null=True)
    series = models.ForeignKey(Series, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.character.name + " in " + self.series.title

