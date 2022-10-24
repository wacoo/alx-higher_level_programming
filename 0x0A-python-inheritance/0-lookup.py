#!/usr/bin/python3

"""A function that returns list of available
attributes and methond in an object"""


def lookup(obj):
    """ return a list of available attributes and classes in the object"""
    return dir(obj)
