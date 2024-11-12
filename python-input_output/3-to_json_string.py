#!/usr/bin/python3
"""Module for returning a json"""
import json


def to_json_string(my_obj):
    """Append a string to a text file and return chars added."""
    return json.dumps(my_obj)
