#!/usr/bin/python3
"""
Defining functio that  return JSON represntation
"""


import json


def to_json_string(my_obj):
    """
    returns string in JSON representation
    """
    return json.dumps(my_obj)
