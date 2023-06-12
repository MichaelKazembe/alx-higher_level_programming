#!/usr/bin/python3
"""
Creates class BaseGeometry
"""


class BaseGeometry():
    """instance of class BaseGeometry"""
    def area(self):
        """ Public instance method area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Public instance method integer validator """
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be an integer")


""" Creates Subclass Rectangle """


class Rectangle(BaseGeometry):
    """ a class Rectangle that inherits from BaseGeometry """
    def __init__(self, width, height):
        """ Initialize subclass Rectangle"""
        if not super().integer_validator("width", width):
            self.__width = width

        if not super().integer_validator("height", height):
            self.__height = height
