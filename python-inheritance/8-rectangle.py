#!/usr/bin/python3
'''create a base geometry class'''


class BaseGeometry:
    '''raise an exception and validate value'''

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')


class Rectangle(BaseGeometry):
"""Rectangle class inherits from BaseGeometry."""

    def init(self, width, height):
         """Initialize rectangle with width and height."""
        super().init()
        self.integer_validator('width', width)
        self.width = width
        self.integer_validator('height', height)
        self.height = height'
