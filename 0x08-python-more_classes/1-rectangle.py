#!/usr/bin/python3
""" creates class Rectangle """


class Rectangle:
    """ class Rectangle """

    def __init__(self, width=0, height=0):
        """ Initialize the Rectangle object """
        self._width = width
        self._height = height

    @property
    def width(self):
        """ Get the width attribute """
        return self._width

    @width.setter
    def width(self, value):
        """ Set the width attribute """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = value

    @property
    def height(self):
        """ Get the height attribute """
        return self._height

    @height.setter
    def height(self, value):
        """ Set the height attribute """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = value
