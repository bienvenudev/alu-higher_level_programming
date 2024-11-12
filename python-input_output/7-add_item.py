#!/usr/bin/python3
"""Module for creating an obj from JSON file"""
import sys
from os.path import exists
from json import dump, load

def save_to_json_file(obj, filename):
    """Write a Python object to a JSON file."""
    with open(filename, 'w', encoding='utf-8') as file:
        dump(obj, file)


def load_from_json_file(filename):
    """Load a Python object from a JSON file."""
    with open(filename, 'r', encoding='utf-8') as file:
        return load(file)


filename = 'add_item.json'

if exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

my_list.extend(sys.argv[1:])
save_to_json_file(my_list, filename)
