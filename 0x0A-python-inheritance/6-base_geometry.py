#!/usr/bin/python3
"""
Defining a geometry class BaseGeometry
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
