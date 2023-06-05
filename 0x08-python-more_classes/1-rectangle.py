#!/usr/bin/python3
"""
This defines a class Rectangle.
"""


class Rectangle:
    """
    A class representing a rectangle.

    Attributes:
    height: height of the rectangle.
    width: width of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializing a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """
        Get height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """
        Get the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
