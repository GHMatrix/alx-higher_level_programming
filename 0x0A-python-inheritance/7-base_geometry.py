#!/usr/bin/python3
"""
Defining a class BaseGeometry
"""


class BaseGeometry:
    """
    A base class for geometry-related classes.
    """

    def area(self):
        """
        Calculate the area of the geometry.

        Error raised:
            Exception: When called directly, as the area calculation
            is not implemented in the base class.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the given value as an integer.

        Args:
            name (str): The name of the value being validated.
            value: The value to be validated.

        Error raised:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
