from django.db import models


class Character(models.Model):
    def __init__(self):
        self.state = models.CharField(max_length=4, null=False)
        self.name = models.CharField(max_length=200)
        self.description = models.CharField(max_length=1000)
        self.image = models.URLField()

    def __str__(self) -> str:
        return self.name


class Comic(models.Model):
    def __init__(self):
        self.title = models.CharField(max_length=200)
        self.description = models.CharField(max_length=500)
        self.image = models.URLField()

    def __str__(self) -> str:
        return self.name


class Series(models.Model):
    def __init__(self):
        self.title = models.CharField(max_length=200)
        self.description = models.CharField(max_length=500)
        self.image = models.URLField()

    def __str__(self) -> str:
        return self.name 


class CharacterInComic(models.Model):
    def __init__(self):
        self.character = models.ForeignKey(Character, on_delete=models.CASCADE)
        self.comic = models.ForeignKey(Comic, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.character.name + " in " + self.comic.name


class CharacterInSeries(models.Model):
    def __init__(self):
        self.character = models.ForeignKey(Character, on_delete=models.CASCADE)
        self.series = models.ForeignKey(Series, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.character.name + " in " + self.series.name

