#!/usr/bin/python3
def raise_exception():
    try:
        result = 1 / 0
    except ZeroDivisionError:
        raise TypeError
    return result
