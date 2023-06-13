#!/usr/bin/python3
"""
Defining function that writes object to file
"""


import json


def save_to_json_file(my_obj, filename):
    """
    writes object to file using JSON
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
