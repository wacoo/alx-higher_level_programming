#!/usr/bin/python3

"""Write a function that returns true if an object is a descendant
of of a class, else false"""


def inherits_from(obj, a_class):
    """return true if obj is a descendant of a_class, else false"""
    if issubclass(type(obj), a_class) and not type(obj) is a_class:
        return True
    else:
        return False
