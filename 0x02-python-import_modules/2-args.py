#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    length_count = len(sys.argv) - 1
    if length_count == 0:
        print("0 arguments.")
    elif length_count == 1:
        print("1 argument:")
    else:
        print(f"{length_count} arguments:")

    for i in range(length_count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
