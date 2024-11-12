#!/usr/bin/python3
"""Module for writing an obj to text file"""
import json


def save_to_json_file(my_obj, filename):
    """function for writing using json string"""
    with open(filename, 'a', encoding='utf-8') as file:
        json.dump(my_obj, file)
