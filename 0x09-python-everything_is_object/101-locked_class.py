#!/usr/bin/python3
"""
This defines a class LockedClass.
"""


class LockedClass:
    """
    LockedClass is a class that restricts dynamically creating
    new instance attributes, except for 'first_name'.

    Attributes:
        first_name (str): The allowed instance attribute 'first_name'.
    """

    __slots__ = ["first_name"]

    def __setattr__(self, name, value):
        if not hasattr(self, name) and name != "first_name":
            raise AttributeError(
                    f"'LockedClass' object has no attribute '{name}'")
        super().__setattr__(name, value)
