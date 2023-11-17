import json
from ..models.marvel_models import Character, Comic, Series, CharacterInComic, CharacterInSeries
import os

def access_json_file(path):
    module = os.path.dirname(__file__)
    file = os.path.join(module, path)
    return file

def create_characters():
    with open(access_json_file("marvel_data\marvel_characters.json"), 'r') as characters_file:
        characters = json.load(characters_file)
    for character in characters:
        Character.objects.create(
            name=character['name'],
            description=character['description'],
            image=character['thumbnail_path'] + '/portrait_fantastic.jpg'
        )


def create_comics():
    with open(access_json_file("marvel_data\marvel_comics.json"), 'r') as comics_file:
        comics_data = json.load(comics_file)
    for comic in comics_data:
        Comic.objects.create(
            title = comic['title'],
            description = comic['description'],
            image = comic['thumbnail_path'] + '/portrait_fantastic.jpg'
        )
        for character_name in comic['characters_list']:
            try:
                character = Character.objects.get(name=character_name)
            except character.DoesNotExist:
                pass
            else:
                comic_object = Comic.objects.get(title=comic['title'])
                CharacterInComic.objects.create(character=character, comic=comic_object)

