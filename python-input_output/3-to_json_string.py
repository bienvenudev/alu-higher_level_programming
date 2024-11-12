#!/usr/bin/python3
import json
"""Module for returning a json"""


def to_json_string(my_obj):
    """Append a string to a text file and return chars added."""
    return json.dumps(my_obj)
