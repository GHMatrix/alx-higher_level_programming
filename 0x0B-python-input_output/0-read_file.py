#!/usr/bin/python3
"""
Defining a function that reads text file
"""


def read_file(filename=""):
    """
    Printing file content, UTF-8 to stdout.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
