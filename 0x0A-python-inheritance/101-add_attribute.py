#!/usr/bin/python3
"""Write a function that adds attribute"""


def add_attribute(objectt, attrib, val):
    """add attribute"""
    if not hasattr(objectt, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(objectt, attrib, val)
