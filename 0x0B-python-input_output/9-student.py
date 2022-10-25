#!/usr/bin/python3
"""Writes a class student"""


class Student:
    """ define init"""
    def __init__(self, first_name, last_name, age):
        """initialise"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return __dict__"""
        return self.__dict__
