#!/usr/bin/python3
"""
Defining a class Square from Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class representing a square.

    Attributes:
        Inherited attributes from Rectangle:
            __width (int): The width of the square.
            __height (int): The height of the square.
            __x (int): The x-coordinate of the square's position.
            __y (int): The y-coordinate of the square's position.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square object.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the
            square's position. Defaults to 0.
            y (int, optional): The y-coordinate of the
            square's position. Defaults to 0.
            id (int, optional): The unique identifier of the
            square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The size of the square.

        Errors raised:
            TypeError: If the input is not an integer.
            ValueError: If the size is less than or equal to 0.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of the Square instance.

        Returns:
            str: The string representation of the Square.
        """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)
