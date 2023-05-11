#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    operations = [
        ("+", add, add(a, b)),
        ("-", sub, sub(a, b)),
        ("*", mul, mul(a, b)),
        ("/", div, div(a, b))
    ]

    for operator, operation, result in operations:
        print("{} {} {} = {}".format(a, operator, b, result))
