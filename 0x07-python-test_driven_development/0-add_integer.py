#!/usr/bin/python3

"""A function that adds two integers"""


def add_integer(a, b=98):

    """ adds any tow integers and returns the result """
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
