#!/usr/bin/python3
"""
Defining a subclass of Rectangle called Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square, inheriting from Rectangle.
    """

    def __init__(self, size):
        """
        Initializing a new Square instance.

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
