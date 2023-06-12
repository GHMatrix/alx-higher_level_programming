#!/usr/bin/python3
"""
Defining function which add attributes
"""


def add_attribute(obj, attr, value):
    """
    Add a new attribute to an object if it's possible.

    Args:
        obj: The object to add the attribute to.
        attr: The name of the attribute.
        value: The value of the attribute.

    Errors raised:
        TypeError: If the object can't have a new attribute.
    """
    if not hasattr(obj, '__dict__') and not hasattr(obj, '__slots__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attr, value)
