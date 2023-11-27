#!/usr/bin/python3
"""
Defines class Rectangle
"""

class Rectangle:
    """
    Representation of a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new rectangle.
        Args:
            width: Represents the width of the rectangle.
            height: Represents the height of the rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Get/set the current width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Get/set the current height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value
