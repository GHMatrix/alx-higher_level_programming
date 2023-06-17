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
        Initializing Square object.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the
            square's position. Defaults to 0.
            y (int, optional): The y-coordinate of the
            square's position. Defaults to 0.
            id (int, optional): The unique identifier
            of the square. Defaults to None.
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

    def update(self, *args, **kwargs):
        """
        Assigns attributes to the instance using the arguments.

        Args:
            *args: The positional arguments.
            **kwargs: The keyword arguments representing attribute-value pairs.

        Errors raised:
            TypeError: If any of the keyword
            arguments is not a valid attribute.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
                else:
                    raise TypeError(
                            f"'{key}' is not a valid attribute of Square")
