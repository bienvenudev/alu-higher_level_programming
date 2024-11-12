#!/usr/bin/python3
import json
import sys 
"""Module for creating an obj from JSON file"""


args = sys.argv[1:]

def save_to_json_file(my_obj, filename):
    """function for writing an object to a text file"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
    except FileNotFoundError:
        existing_data = []

    existing_data.extend(my_obj)

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(existing_data, f)


def load_from_json_file(filename):
    """function for creating an object from json string"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

save_to_json_file(args, 'add_item.json')
