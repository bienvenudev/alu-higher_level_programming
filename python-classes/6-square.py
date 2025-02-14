#!/usr/bin/python3
"""Defines an empty class Square."""


class Square:
    """Initialize square with private size"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(i, int) and i >= 0 for i in value)):
            self.__position = value
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            print('\n' * self.__position[1], end="")
            for i in range(self.__size):
                print(' ' * self.__position[0] + "#" * self.__size)
