#!/usr/bin/python3
"""
Defining class Rectangle that inherits from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, inheriting from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __repr__(self):
        """
        Return a string representation of the Rectangle object.

        Returns:
            str: A string representation of the Rectangle object.
        """
        return "<Rectangle(Rectangle) object at {}>".format(hex(id(self)))
