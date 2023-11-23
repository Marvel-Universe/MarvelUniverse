"""Create objects in the models based on the data obtained from the API."""
import json
from MarvelUniverse.models import Character, CharacterQuestion, CharacterChoice, SeriesQuestion, SeriesChoice, ComicQuestion, ComicChoice
import os
import random


def access_json_file(path):
    """Access json file by path"""
    module = os.path.dirname(__file__)
    file = os.path.join(module, path)
    return file


def create_character_quiz():
    """Create question objects for character quiz."""
    with open(access_json_file("marvel_data\marvel_characters.json"), 'r') as characters_file:
        characters = json.load(characters_file)
    for character in characters:
        question = CharacterQuestion.objects.create(
            description=character['description'], 
            image=character['thumbnail_path'] + '/portrait_uncanny.jpg',
        )
        # create 1 correct choice
        CharacterChoice.objects.create(
            question = question,
            character_name = character["name"],
            is_correct = True
        )
        # create incorrect choices with other character names
        random_characters = random.sample(characters, 20)
        other_characters = [c for c in random_characters if c["name"] != character["name"]]
        for other_character in other_characters:
            CharacterChoice.objects.create(
                question=question,
                character_name=other_character["name"],
                is_correct=False
            )


def create_comics_quiz():
    """Create question objects for comic quiz."""
    with open(access_json_file("marvel_data\marvel_characters.json"), 'r') as characters_file:
        characters = json.load(characters_file)
    with open(access_json_file("marvel_data\marvel_comics.json"), 'r') as comics_file:
        comics_data = json.load(comics_file)
    selected_comics = random.sample(comics_data, 100)
    for comic in selected_comics:
        question = ComicQuestion.objects.create(
            title=comic['title'],
            description=comic['description'],
            image=comic['thumbnail_path'] + '/portrait_uncanny.jpg'
        )
        # create correct choices
        for character_name in comic['characters_list']:
            try:
                character = Character.objects.get(name=character_name)
            except Character.DoesNotExist:
                pass
            else:
                ComicChoice.objects.create(
                    question=question,
                    character_name=character.name,
                    character_image=character.image,
                    is_correct=True
                )
        # create incorrect choices
        random_characters = random.sample(characters, 20)
        for other_character in random_characters:
            if other_character["name"] not in comic['characters_list']:
                ComicChoice.objects.create(
                    question=question,
                    character_name=other_character["name"],
                    character_image=other_character['thumbnail_path'] + '/portrait_uncanny.jpg',
                    is_correct=False
                )


def create_series_quiz():
    """Create question objects for series quiz."""
    with open(access_json_file("marvel_data\marvel_characters.json"), 'r') as characters_file:
        characters = json.load(characters_file)
    with open(access_json_file("marvel_data\marvel_series.json"), 'r') as comics_file:
        series_data = json.load(comics_file)
    selected_series = random.sample(series_data, 100)
    for series in selected_series:
        question = SeriesQuestion.objects.create(
            title=series['title'],
            description=series['description'],
            image=series['thumbnail_path'] + '/portrait_uncanny.jpg'
        )   
        # create correct choices
        for character_name in series['characters_list']:
            try:
                character = Character.objects.get(name=character_name)
            except Character.DoesNotExist:
                pass
            else:
                SeriesChoice.objects.create(
                    question=question,
                    character_name=character.name,
                    character_image=character.image,
                    is_correct=True
                )
        # create incorrect choices
        random_characters = random.sample(characters, 20)
        for other_character in random_characters:
            if other_character["name"] not in series['characters_list']:
                SeriesChoice.objects.create(
                    question=question,
                    character_name=other_character["name"],
                    character_image=other_character['thumbnail_path'] + '/portrait_uncanny.jpg',
                    is_correct=False
                )
