#!/usr/bin/python3

"""Write a class Rectangle that inherits BaseGeopmetry"""
bg = __import__("7-base_geometry")


class Rectangle(bg.BaseGeometry):
    """ This class is  a child of BaseGeometry"""
    def __init__(self, width, height):
        """init object"""
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)
