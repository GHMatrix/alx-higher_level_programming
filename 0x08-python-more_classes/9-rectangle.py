#!/usr/binpython3
"""
This defines a class Rectangle.
"""


class Rectangle:
    """
    A class representing a rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle instance.

        Args:
        width: width of the rectangle. Default is 0.
        height: height of the rectangle. Default is 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """
        Delete a Rectangle instance and print a farewell message.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """
        Retrieve the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
        value: The width value to set.

        Errors raised:
        TypeError: If the width is not an integer.
        ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieve the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
        value: The height value to set.

        Errors raised:
        TypeError: If the height is not an integer.
        ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Determine area of the rectangle.

        Returns:
        int: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Determine the perimeter of the rectangle.

        Returns:
        - int: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
        str: The string representation of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ""
        symbol = str(self.print_symbol)
        rectangle = symbol * self.width
        return "\n".join([rectangle] * self.height)

    def __repr__(self):
        """
        Return a string representation of the rectangle object.

        Returns:
        - str: The string representation of the rectangle object.
        """
        return f"Rectangle({self.width}, {self.height})"

    @classmethod
    def square(cls, size):
        """
        Create a square with equal width and height.

        Args:
        size: size of the square.

        Returns:
        Rectangle: The created square.
        """
        return cls(size, size)
