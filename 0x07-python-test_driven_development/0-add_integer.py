#!/usr/bin/python3
"""
Defining an integer addition function.
"""


def add_integer(a, b=98):
    """Adds two integers and returns the result.

    Arguments:
    num1 (int or float) -- The first number.
    num2 (int or float) -- The second number (default is 98).

    Returns:
    int: The addition of a and b, casted to an integer.

    Error raised:
    TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
