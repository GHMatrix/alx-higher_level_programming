#!/usr/bin/python3
for c in range(ord('z'), ord('a')-1, -1):
    if (ord('z')-c) % 2 == 0:
        print(f"{chr(c)}", end="")
    else:
        print(f"{chr(c-32)}", end="")
