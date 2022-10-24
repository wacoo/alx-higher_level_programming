#!/usr/bin/python3

"""Check if an obeject is an instance of a given class """


def is_same_class(obj, a_class):

    """ Return true if same class, else return false"""
    if type(obj) == a_class:
        return True
    else:
        return False
