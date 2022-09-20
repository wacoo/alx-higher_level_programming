#!/usr/bin/python3
def print_last_digit(number):
    str = repr(number)
    digit = str[-1]
    print(digit, end='')
    return digit
