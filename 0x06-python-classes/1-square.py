#!/usr/bin/python3
"""
Defining a class Square
"""


class Square:
    """
    This represents a square.

    This class defines a square by size, which is private instance attribute.
    """

    def __init__(self, size):
        """
        Initializing new instance of the Square class.

        Args:
            size (int): Size of the square.
        """
        self.__size = size
