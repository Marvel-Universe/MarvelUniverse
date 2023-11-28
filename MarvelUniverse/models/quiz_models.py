from django.db import models


class CharacterQuestion(models.Model):

    description = models.TextField()
    image = models.URLField(null=True)

    def __str__(self) -> str:
        return self.description


class CharacterChoice(models.Model):

    question = models.ForeignKey(CharacterQuestion, on_delete=models.CASCADE, null=True)
    character_name = models.CharField(max_length=200, null=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.character_name
    

class ComicQuestion(models.Model):

    title = models.CharField(max_length=200, null=True)
    description = models.TextField()
    image = models.URLField()

    def __str__(self) -> str:
        return self.title
    

class ComicChoice(models.Model):

    question = models.ForeignKey(ComicQuestion, on_delete=models.CASCADE, null=True)
    character_name = models.CharField(max_length=200, null=True)
    character_image = models.URLField(null=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.character_name
    

class SeriesQuestion(models.Model):

    title = models.CharField(max_length=200, null=True)
    description = models.TextField()
    image = models.URLField()

    def __str__(self) -> str:
        return self.title
    

class SeriesChoice(models.Model):

    question = models.ForeignKey(SeriesQuestion, on_delete=models.CASCADE, null=True)
    character_name = models.CharField(max_length=200, null=True)
    character_image = models.URLField(null=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.character_name
