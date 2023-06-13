#!/usr/bin/python3
"""
Defining function that takes JSON string
"""


import json


def from_json_string(my_str):
    """
    returns object from JSON string
    """
    return json.loads(my_str)
