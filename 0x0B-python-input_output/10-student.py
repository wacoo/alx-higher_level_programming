#!/usr/bin/python3

"""Writes a class student"""


class Student:
    """ define init"""
    def __init__(self, first_name, last_name, age):
        """initialise"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """ define a function that returns a json rep of student instance"""
    def to_json(self, attrs=None):
        """return __dict__"""
        if (type(attrs) == list and all(type(e) == str for e in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
