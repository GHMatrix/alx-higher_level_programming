#!/usr/bin/python3
"""
Defining class MyInt that inherits from int
"""


class MyInt(int):
    """
    A class representing an integer.
    """

    def __eq__(self, other):
        """
        Check if the value is not equal to the other value.

        Args:
            other: The value to compare.

        Returns:
            bool: True if not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Check if the value is equal to the other value.

        Args:
            other: The value to compare.

        Returns:
            bool: True if equal, False otherwise.
        """
        return super().__eq__(other)
