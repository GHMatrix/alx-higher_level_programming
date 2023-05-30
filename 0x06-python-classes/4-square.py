#!/usr/bin/python3
"""
Defining a class Square
"""

class Square:
    """
    Represents a square.

    This class defines a square by its size, a private instance attribute.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Parameters:
            size (int, optional): The size of the square. Default is 0.

        Errors raised:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0.
        """
        self.__size = 0  # Initialize the private instance attribute __size
        self.size = size  # Set the size using the setter property

    @property
    def size(self):
        """
        Retrieve the current size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Parameters:
            value (int): The size of the square.

        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Determine  and return the current area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
