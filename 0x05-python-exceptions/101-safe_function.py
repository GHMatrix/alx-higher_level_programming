#!/usr/bin/python3

import sys
import traceback


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as e:
        traceback.print_exc(file=sys.stderr)
        return None
