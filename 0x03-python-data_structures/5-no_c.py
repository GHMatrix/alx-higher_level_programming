#!/usr/bin/python3
def no_c(my_string):
    copy = ''.join([x for x in my_string if x.lower() != 'c'])
    return copy
