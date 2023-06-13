#!/usr/bin/python3
"""
Defining script that adds all arguments
"""


import sys


from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


def main():
    """
    Adds command line arguments to a Python list and saves them to a JSON file.

    Command line arguments:
        The command line arguments provided when running the script.

    JSON file:
        The file to which the list will be saved in JSON format.
    """
    filename = "add_item.json"

    try:
        json_list = load_from_json_file(filename)
    except FileNotFoundError:
        json_list = []

    for arg in sys.argv[1:]:
        json_list.append(arg)

    save_to_json_file(json_list, filename)
