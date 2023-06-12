#!/usr/bin/python3
"""
Defining a class that checks instance of specified class
"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is an instance of the
        specified class; False otherwise.
    """
    return type(obj) is a_class
