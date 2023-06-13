#!/usr/bin/python3
"""
Defining function that takes from object
"""


def class_to_json(obj):
    """
    this returns returns the dictionary description with
    simple data structure
    """
    return obj.__dict__
