#!/usr/bin/python3
"""
Defining a class Square
"""


class Square:
    """
    Represents a square.

    This class defines a square by its size, is a private instance attribute.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int, optional): The size of the square. Default is 0.

        Error raised:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
