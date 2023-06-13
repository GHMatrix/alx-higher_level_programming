#!/usr/bin/python3
"""
Defining function that appends string
"""


def append_write(filename="", text=""):
    """
    returns number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
