#!/usr/bin/python3
"""Module for student class."""


class Student:
    """A class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve the dictionary representation of student."""
        return self.__dict__
