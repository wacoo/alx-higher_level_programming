#!/usr/bin/python3

"""Write an empty class BaseGeometry"""


class BaseGeometry:
    """has a method that raises an exception"""
    def area(self):
        """ raises an exception """
        raise Exception("area() is not implemented")
