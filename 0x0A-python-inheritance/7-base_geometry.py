#!/usr/bin/python3

"""Write an empty class BaseGeometry"""


class BaseGeometry:
    """has a method that raises an exception"""
    def area(self):
        """ raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates given value"""
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
