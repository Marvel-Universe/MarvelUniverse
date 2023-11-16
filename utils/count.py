"""Count the number of items in json file/"""
import json

# Specify the JSON file's filename
json_filename = "marvel_data/marvel_series.json"  # Replace with the actual filename

try:
    with open(json_filename, "r") as json_file:
        data = json.load(json_file)
        count = len(data)
        print(f"The number of items in the JSON file '{json_filename}' is: {count}")
except FileNotFoundError:
    print(f"The JSON file '{json_filename}' was not found.")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON data: {e}")
