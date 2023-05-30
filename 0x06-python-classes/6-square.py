#!/usr/bin/python3
"""
Defining a class Square
"""


class Square:
    """
    Represents a square.

    This class defines square by its size and
    position,both private instance attributes.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Parameters:
            size (int, optional): The size of the square. Default is 0.
            position (tuple, optional): The position of the
            square. Default is (0, 0).

        Raises:
            TypeError: If size is not an integer or
            position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0 or
            position contains negative integers.
        """
        self.__size = 0
        self.__position = (0, 0)
        self.size = size
        self.position = position

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

        Errors raised:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieve the current position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Parameters:
            value (tuple): The position of the square.

        Raises:
            TypeError: If the provided position
            is not a tuple of 2 positive integers.
            ValueError: If the provided position contains negative integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(coord, int)
                        and coord >= 0 for coord in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Determines and return the current area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the '#' character.

        If size is equal to 0, prints an empty line.
        If position[1] is greater than 0, adjusts the printing by using spaces.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
