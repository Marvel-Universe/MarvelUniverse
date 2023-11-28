from django.db import models


class Character(models.Model):
    """
    Model to represent a character in the Marvel Universe.

    Attributes:
    - name (str): The name of the character.
    - description (str): A brief description of the character.
    - image (str): The URL of the character's image.

    """
    name = models.CharField(max_length=200, null=True)
    description = models.TextField()
    image = models.URLField(null=True)

    def __str__(self) -> str:
        """
        Methods:
        - __str__(): Returns the name of the character as a string.
        """
        return self.name


class Comic(models.Model):
    """
    Model to represent a comic in the Marvel Universe.

    Attributes:
    - title (str): The title of the comic.
    - description (str): A brief description of the comic.
    - image (str): The URL of the comic's image.
    """
    title = models.CharField(max_length=200, null=True)
    description = models.TextField()
    image = models.URLField(null=True)

    def __str__(self) -> str:
        """
        Methods:
        - __str__(): Returns the title of the comic as a string.
        """
        return self.title


class Series(models.Model):
    """
    Model to represent a series in the Marvel Universe.

    Attributes:
    - title (str): The title of the series.
    - description (str): A brief description of the series.
    - image (str): The URL of the series' image.
    """
    title = models.CharField(max_length=200, null=True)
    description = models.TextField()
    image = models.URLField(null=True)

    def __str__(self) -> str:
        """
        Methods:
        - __str__(): Returns the title of the series as a string.
        """
        return self.title


class CharacterInComic(models.Model):
    """
    Model to represent the relationship between a character and a comic.

    Attributes:
    - character (Character): The character in the relationship.
    - comic (Comic): The comic in the relationship.
    """
    character = models.ForeignKey(Character, on_delete=models.CASCADE, null=True)
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        """
        Methods:
        - __str__(): Returns a string representation of the relationship.
        """
        return self.character.name + " in " + self.comic.title


class CharacterInSeries(models.Model):
    """
    Model to represent the relationship between a character and a series.

    Attributes:
    - character (Character): The character in the relationship.
    - series (Series): The series in the relationship.
    """
    character = models.ForeignKey(Character, on_delete=models.CASCADE, null=True)
    series = models.ForeignKey(Series, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        """
        Methods:
        - __str__(): Returns a string representation of the relationship.
        """
        return self.character.name + " in " + self.series.title
