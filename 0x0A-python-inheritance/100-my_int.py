#!/usr/bin/python3

"""Write a class that inherits from int"""


class MyInt(int):

    """ Defines init and eq methods """

    def __eq__(self, other):
        """ when two numbers are equal"""
        return self.real != other

    def __ne__(self, other):
        """when two numbers are not equal"""
        return self.real == other
