#!/usr/bin/python3
"""
Defining function that creates object
"""


import json


def load_from_json_file(filename):
    """
    creates Object from a JSON file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
