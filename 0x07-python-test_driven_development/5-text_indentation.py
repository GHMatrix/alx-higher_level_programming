#!/usr/bin/python3
"""
Defining a function that prints text with two new
lines after each of these characters:  ., ? and :
"""


def text_indentation(text):
    """
    Print a text with 2 new lines after each occurrence of '.', '?', and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = ['.', '?', ':']
    lines = text.splitlines()

    for line in lines:
        formatted_line = line.strip()
        if any(p in formatted_line for p in punctuation):
            formatted_line = formatted_line.replace(".", "\n\n")
            formatted_line = formatted_line.replace("?", "\n\n")
            formatted_line = formatted_line.replace(":", "\n\n")
        print(formatted_line)


if __name__ == "__main__":
    text_indentation("Hello. How are you? Fine: Thank you!")
    text_indentation("This is a test.")
    text_indentation("No punctuation")
