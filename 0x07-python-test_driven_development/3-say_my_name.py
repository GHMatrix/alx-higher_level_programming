#!/usr/bin/python3
"""
Defining a function that prints names
"""


def say_my_name(first_name, last_name=""):
    """
    Print "My name is <first name> <last name>".

    Args:
        first_name (str): The first name.
        last_name (str): The last name (default is an empty string).

    Errors raised:
        TypeError: If either first_name or last_name is not a string.

    Example:
        >>> say_my_name("John", "Doe")
        My name is John Doe

        >>> say_my_name("Jane")
        My name is Jane
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    full_name = first_name
    if last_name:
        full_name += " " + last_name

    print("My name is", full_name)


if __name__ == "__main__":
    say_my_name("John", "Doe")
    say_my_name("Jane")
