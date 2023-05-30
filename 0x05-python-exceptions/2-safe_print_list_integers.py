#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for item in my_list[:x]:
        if isinstance(item, int):
            try:
                print("{:d}".format(item), end="")
                count += 1
            except (ValueError, TypeError):
                continue
    print("")
    return count