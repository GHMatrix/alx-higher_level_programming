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
    attributes = []
    methods = []

    for item in dir(obj):
        if not item.startswith('__') and not callable(getattr(obj, item)):
            attributes.append(item)
        elif callable(getattr(obj, item)):
            methods.append(item)

    return attributes + methods
