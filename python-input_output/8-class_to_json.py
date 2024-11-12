#!/usr/bin/python3
"""Module for to convert JSON"""


def class_to_json(obj):
    """Return dictionary for JSON serialization"""
    return obj.__dict__
