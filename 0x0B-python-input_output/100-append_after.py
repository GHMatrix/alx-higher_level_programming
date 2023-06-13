#!/usr/bin/python3
"""
Defining a function that inserts line of text
to a file
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Appends a line of text after each line
    containing a specific string in a file.

    Parameters:
    filename (str): The name of the file to modify.
    search_string (str): The string to search for in each line of the file.
    new_string (str): The line of text to insert after each matching line.

    Returns:
    None
    """
    # Open the file in read mode and read all lines into a list
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    line_list = []
    for line in lines:
        # Append the current line to the list
        line_list.append(line)
        if search_string in line:
            # If the search string is found in the line, append the new string
            line_list.append(new_string)

    # Open the file in write mode and write the modified lines back to the file
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(line_list)
