#!/usr/bin/python3
"""Module for creating an obj from JSON file"""
import json


def load_from_json_file(filename):
    """function for creating an object from json string"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
