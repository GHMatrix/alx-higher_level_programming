#!/usr/bin/python3
"""
Defining a function that writes string to a file
and counts characters
"""


def write_file(filename="", text=""):
    """
    Returns number of characters in a text file
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)
            return len(text)
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
