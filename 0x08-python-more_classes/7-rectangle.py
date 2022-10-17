#!/usr/bin/python3

""" Empty class Rectangle """


class Rectangle:

    """ Rectangle class"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Init a rectangle"""
        if isinstance(int(width), int):
            width = int(width)
        if isinstance(int(height), int):
            height = int(height)
        if type(int(width)) != int:
            raise TypeError("width must be an integer")
        elif type(int(height)) != int:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        elif height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height
        self.print_symbol = Rectangle.print_symbol

        Rectangle.number_of_instances += 1

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
        self.__height = value

    def area(self):
        """calculate area"""
        return self.__width * self.__height

    def perimeter(self):
        """calculate perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ Print rectangle"""
        r = []
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    r.append(str(self.print_symbol))
                if i != self.__height - 1:
                    r.append("\n")
            return ("". join(r))

    def __repr__(self):
        """ print rectangle with repr"""
        return "Rectangle({}, {}".format(self.__width, self.__height) + ")"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
