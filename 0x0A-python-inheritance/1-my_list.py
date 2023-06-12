#!/usr/bin/python3
"""
Defining class MyList that inherits from another class
"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.

    Class provides a method to print the list elements in sorted order.

    Attributes:
        Inherits all attributes from the built-in list class.

    Methods:
        print_sorted(): Prints the list elements in ascending sorted order.
    """
    def print_sorted(self):
        """
        Prints sorted list in ascending porter
        """
        sorted_list = sorted(self)
        print(sorted_list)
