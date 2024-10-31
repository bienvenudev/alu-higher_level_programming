#!/usr/bin/python3
"""Defines an empty class Square."""


class Square:
    """Initialize square with private size"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
