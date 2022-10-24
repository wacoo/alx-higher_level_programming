#!/usr/bin/python3

""" Write a function that returns true if a given object
is an instance of a given class or an instance of a parent
class of a given class """


def is_kind_of_class(obj, a_class):
    """Return true if obj is an instance of a_class, else return false"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
