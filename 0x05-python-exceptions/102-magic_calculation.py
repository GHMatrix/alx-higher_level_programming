#!/usr/bin/python3

def magic_calculation(a, b):
    try:
        result = sum(a ** b / i for i in range(1, 3) if i <= a)
    except Exception:
        result = b + a
    return result
