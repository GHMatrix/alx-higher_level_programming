#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    is_list = isinstance(my_list, list)
    if is_list:
        reversed_list = my_list[::-1]
        for i in reversed_list:
            print("{:d}".format(i))
