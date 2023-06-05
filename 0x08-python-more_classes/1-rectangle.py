#!/usr/bin/python3
""" creates class Rectangle """


class Rectangle:
    """ class Rectangle """

    def __init__(self, width=0, height=0):
        """ Initialize the Rectangle object """
        self._width = width
        self._height = height

    @property
    def height(self):
        """ Get the height attribute """
        return self._height

    @property
    def width(self):
        """ Get the width attribute """
        return self._width

    @height.setter
    def height(self, value):
        """ Sets height attribute """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    @width.setter
    def width(self, value):
        """ Set width attribute """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value
