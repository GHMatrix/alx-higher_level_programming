#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in my_list:
            print(i, end='')
            count += 1
            if count == x:
                break
        print()
        return count
    except Exception as e:
        print("An error occurred:", e)
        return count
