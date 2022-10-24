#!/usr/bin/python3

"""Write a class Rectangle that inherits BaseGeopmetry"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Class rectagle with two methods"""
    def __init__(self, size):
        """init method"""
        self.__size = size
        super().integer_validator("size", self.__size)

    def area(self):
        """area method"""
        return self.__size * self.__size

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
