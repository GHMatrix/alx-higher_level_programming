#!/usr/bin/python3
"""
Defining a function that prints a square with character #
"""


def print_square(size):
    """
    Print a square with the character #.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer or a float.
        ValueError: If size is less than 0.
        TypeError: If size is a float and less than 0.

    """
    if not isinstance(size, int) and not isinstance(size, float):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)


if __name__ == "__main__":
    print_square(5)
    print_square(3)
    print_square(0)
    print_square(-2)
    print_square(2.5)
