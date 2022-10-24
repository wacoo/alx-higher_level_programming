#!/usr/bin/python3

"""Write a class Rectangle that inherits BaseGeopmetry"""
bg = __import__("7-base_geometry")


class Rectangle(bg.BaseGeometry):
    """Class rectagle with two methods"""
    def __init__(self, width, height):
        """init method"""
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)

    def area(self):
        """area method"""
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
