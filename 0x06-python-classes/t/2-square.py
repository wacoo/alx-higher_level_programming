#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise ValueError("size must be >= 0")
        elif size < 0:
            raise TypeError("size must be an integer")
        self.__size = size
