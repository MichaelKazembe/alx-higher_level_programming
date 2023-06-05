#!/usr/bin/python3
""" creates class Rectangle """


class Rectangle:
    """ class Rectangle """

    def __init__(self, width=0, height=0):
        """ Initialize the Rectangle object """
        self.width = width
        self.height = height

    @property
    def height(self):
        """ Get the height attribute """
        return self.__height

    @property
    def width(self):
        """ Get the width attribute """
        return self.__width

    @height.setter
    def height(self, value):
        """ Sets height attribute """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """ Set width attribute """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """ Calculates area of rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Calculates perimeter of rectangle """
        if self.__width == 0 or self.__height == 0:
            return None
        return 2 * (self.__width + self.__height)
