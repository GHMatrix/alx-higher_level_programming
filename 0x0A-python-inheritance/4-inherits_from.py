#!/usr/bin/python3
"""
Defining class that checks inheritance
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class;
        otherwise, False.
    """
    if isinstance(obj, type):
        # Check if the object itself is a class
        return issubclass(obj, a_class)
    else:
        # Check if any of the object's classes inherit from the specified class
        return any(issubclass(cls, a_class) for cls in obj.__class__.mro()[1:])
