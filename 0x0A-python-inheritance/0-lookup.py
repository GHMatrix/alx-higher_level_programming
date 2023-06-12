#!/usr/bin/python3
"""
Defining an attribue of an obj lookup
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list containing the available attributes and methods of the object.
    """
    return (dir(obj))
