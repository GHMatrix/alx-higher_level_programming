#!/usr/bin/python3
"""
Defining Square class that inhertis from Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square.

    This class inherits from the Rectangle class and
    provides functionality to squares.
    """

    def __init__(self, size):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square.
        """
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Return a string representation of the Square.

        Returns:
            str: A string representation of the Square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
