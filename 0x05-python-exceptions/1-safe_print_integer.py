#!/usr/bin/python3
def safe_print_integer(value):
    success = True
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError):
        success = False
    finally:
        return success
