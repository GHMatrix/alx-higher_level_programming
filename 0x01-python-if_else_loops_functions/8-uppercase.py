#!/usr/bin/python3
def uppercase(s):
    """Print a string in uppercase."""
    for c in s:
        if 'a' <= c <= 'z':
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
