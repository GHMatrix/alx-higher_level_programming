#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
    digit *= -1

output_string = f"Last digit of {number} is {digit} and is "

if digit > 5:
    output_string += "greater than 5"
elif digit == 0:
    output_string += "0"
else:
    output_string += "less than 6 and not 0"

print(output_string)
