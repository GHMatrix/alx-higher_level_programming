#!/usr/bin/python3
"""
Defining a function that writes string to a file
and counts characters
"""


def write_file(filename="", text=""):
    """
    Returns number of characters in a text file
    """
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
