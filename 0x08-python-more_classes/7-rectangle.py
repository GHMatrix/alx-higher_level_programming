#!/usr/bin/python3
"""
This defines a class Rectangle.
"""


class Rectangle:
    """
    A class representing a rectangle.

    Attributes:
    width: width of the rectangle.
    height: height of the rectangle.
    number_of_instances (int): The count of rectangle instances created.
    print_symbol: The symbol used for string representation of the rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a rectangle object.

        Args:
        width: The width of the rectangle (default: 0).
        height: The height of the rectangle (default: 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
        - int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
        value: The width value to set.

        Raises:
        - TypeError: If width is not an integer.
        - ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
        - int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
        - value: The height value to set.

        Raises:
        - TypeError: If height is not an integer.
        - ValueError: If height is less than 0.
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
        - int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
        - int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return a string representation of the rectangle.

        The rectangle is represented using the print_symbol.

        Returns:
        - str: The string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += str(self.print_symbol) * self.__width + "\n"
        return rectangle_str[:-1]

    def __repr__(self):
        """
        Return a string representation of the rectangle object.

        Returns:
        - str: The string representation of the rectangle object.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Perform cleanup when the rectangle object is deleted.

        Prints a farewell message
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
