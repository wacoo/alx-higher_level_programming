#!/usr/bin/python3

""" Empty class Rectangle """


class Rectangle:

    """ Rectangle class"""

    def __init__(self, width=0, height=0):
        """ Init a rectangle"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif type(height) != int:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        elif height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """calculate area"""
        return self.__width * self.__height

    def perimeter(self):
        """calculate perimeter"""
        if (self.__width == 0 or self.__height == 0):
            return 0
        return 2 * (self.__width + self.__height)
