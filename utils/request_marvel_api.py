"""Request Marvel API and save to json file."""
from decouple import config
import hashlib, time, requests, json


def generate_api_url(title: str):
    """Define the base API URL."""
    api_url = f"http://gateway.marvel.com/v1/public/{title}"
    timestamp = str(int(time.time()))
    private_key = config('PRIVATE_KEY')    
    public_key = config('PUBLIC_KEY')
    hash_string = timestamp + private_key + public_key
    md5_hash = hashlib.md5(hash_string.encode()).hexdigest()
    api_params = {
        "ts": timestamp,
        "apikey": public_key,
        "hash": md5_hash,
        "limit": 100,
    }
    return api_url, api_params


def get_characters(api_url, api_params):
    """Request characters data from Marvel API."""
    characters_data = []

    for letter in range(ord('a'), ord('z') + 1):
        api_params["nameStartsWith"] = chr(letter)

        response = requests.get(api_url, params=api_params)

        if response.status_code == 200:
            api_data = response.json()
            results = api_data["data"]["results"]
            for result in results:
                name = result["name"]
                description = result["description"]
                thumbnail_path = result["thumbnail"]["path"]
                comics_list = [item["name"] for item in result["comics"]["items"]]
                comics_url = result["comics"]["collectionURI"]
                series_list = [item["name"] for item in result["series"]["items"]]
                series_url = result["series"]["collectionURI"]
                if description and thumbnail_path != "http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available":
                    character_info = {
                        "name": name,
                        "description": description,
                        "thumbnail_path": thumbnail_path,
                        "comics_url": comics_url,
                        "series_url": series_url,
                        "comics_list": comics_list,
                        "series_list": series_list
                    }
                    characters_data.append(character_info)
        else:
            print(f"Failed to retrieve data for letter '{chr(letter)}'. Status code: {response.status_code}")

    # Write the characters data to the JSON file
    with open("marvel_data\marvel_characters.json", "w") as json_file:
        json.dump(characters_data, json_file, indent=4)


def get_comics(api_params):
    """Request comics data from Marvel API."""
    # read Marvel characters data from json file
    with open("marvel_data\marvel_characters.json", 'r') as character_file:
        characters = json.load(character_file)
    filtered_data = []
    added_titles = [] 
    for character in characters:
        url = character[f"comics_url"]
        response = requests.get(url, params=api_params)
        if response.status_code == 200:
            data = response.json()
            for result in data['data']['results']:

                title = result['title']
                thumbnail_path = result['thumbnail']['path']
                characters_url = result['characters']["collectionURI"]
                characters_list = [character['name'] for character in result['characters']['items']]
                if thumbnail_path != "http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available":
                    if result["textObjects"] and title not in added_titles:
                        filtered_data.append({
                            "title": title,
                            "description": result["textObjects"][0]["text"],
                            "thumbnail_path": thumbnail_path,
                            "characters_url": characters_url,
                            "characters_list": characters_list
                        })
                        added_titles.append(title)
        else:
            print(response.status_code)
    # Save the Marvel comics data to a new JSON file
    with open("marvel_data\marvel_comics.json", 'w') as filtered_file:
        json.dump(filtered_data, filtered_file, indent=4)


def get_series(api_params):
    """Request series data from Marvel API."""
    # read Marvel characters data from json file
    with open("MarvelUniverse\marvel_characters.json", 'r') as character_file:
        characters = json.load(character_file)
    filtered_data = []
    added_titles = [] 
    for character in characters:
        url = character[f"series_url"]
        response = requests.get(url, params=api_params)
        if response.status_code == 200:
            data = response.json()
            for result in data['data']['results']:
                title = result['title']
                description = result["description"]
                thumbnail_path = result['thumbnail']['path']
                characters_url = result['characters']["collectionURI"]
                characters_list = [character['name'] for character in result['characters']['items']]
                if result['thumbnail']['path'] != "http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available":
                    if result["description"] and title not in added_titles:
                        filtered_data.append({
                            "title": title,
                            "description": description,
                            "thumbnail_path": thumbnail_path,
                            "characters_url": characters_url,
                            "characters_list": characters_list
                        })
                        added_titles.append(title)
        else:
            print(response.status_code)
    # Save the Marvel series data to a new JSON file
    with open("marvel_data\marvel_series.json", 'w') as filtered_file:
        json.dump(filtered_data, filtered_file, indent=4)


def get_character_in_comics(api_params):
    """Request characters data which in the comics from Marvel API."""
    with open("marvel_data\marvel_characters.json", 'r') as character_file:
        characters = json.load(character_file)
    with open("marvel_data\marvel_comics.json", 'r') as comic_file:
        comics = json.load(comic_file)
    character_name = [character['name'] for character in characters]
    filtered_data = []
    for comic in comics:
        url = comic[f"characters_url"]
        response = requests.get(url, params=api_params)
        if response.status_code == 200:
            data = response.json()
            for result in data['data']['results']:
                name = result["name"]
                description = result["description"]
                thumbnail_path = result["thumbnail"]["path"]
                comics_list = [item["name"] for item in result["comics"]["items"]]
                comics_url = result["comics"]["collectionURI"]
                series_list = [item["name"] for item in result["series"]["items"]]
                series_url = result["series"]["collectionURI"]
                if result['thumbnail']['path'] != "http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available":
                    if result["description"] and name not in character_name:
                        character_info = {
                            "name": name,
                            "description": description,
                            "thumbnail_path": thumbnail_path,
                            "comics_url": comics_url,
                            "series_url": series_url,
                            "comics_list": comics_list,
                            "series_list": series_list
                        }
                        filtered_data.append(character_info)
                        character_name.append(name)
        else:
            print(response.status_code)
    # Save the Marvel series data to a new JSON file
    with open("marvel_data\marvel_characters.json", 'w') as filtered_file:
        json.dump(filtered_data, filtered_file, indent=4)


def get_character_in_series(api_params):
    """Request characters data which in the series from Marvel API."""
    with open("marvel_data\marvel_characters.json", 'r') as character_file:
        characters = json.load(character_file)
    with open("marvel_data\marvel_series.json", 'r') as serie_file:
        series = json.load(serie_file)
    character_name = [character['name'] for character in characters]
    filtered_data = []
    for serie in series:
        url = serie[f"characters_url"]
        response = requests.get(url, params=api_params)
        if response.status_code == 200:
            data = response.json()
            for result in data['data']['results']:
                name = result["name"]
                description = result["description"]
                thumbnail_path = result["thumbnail"]["path"]
                comics_list = [item["name"] for item in result["comics"]["items"]]
                comics_url = result["comics"]["collectionURI"]
                series_list = [item["name"] for item in result["series"]["items"]]
                series_url = result["series"]["collectionURI"]
                if result['thumbnail']['path'] != "http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available":
                    if result["description"] and name not in character_name:
                        character_info = {
                            "name": name,
                            "description": description,
                            "thumbnail_path": thumbnail_path,
                            "comics_url": comics_url,
                            "series_url": series_url,
                            "comics_list": comics_list,
                            "series_list": series_list
                        }
                        filtered_data.append(character_info)
                        character_name.append(name)
        else:
            print(response.status_code)
    # Save the Marvel series data to a new JSON file
    with open("marvel_data\marvel_characters.json", 'w') as filtered_file:
        json.dump(filtered_data, filtered_file, indent=4)

# base url for Marvel characters
characters_api_url, api_params = generate_api_url("characters")
# get Marvel characters data
get_characters(characters_api_url, api_params)

# base url for Marvel comics
comics_api_url, api_params = generate_api_url("comics")
# get Marvel comics data
get_comics(api_params)
get_character_in_comics(api_params)

# base url for Marvel series
series_api_url, api_params = generate_api_url("series")
# get Marvel series data
get_series(api_params)
get_character_in_series(api_params)
