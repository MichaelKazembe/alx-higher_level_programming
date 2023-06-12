#!/usr/bin/python3
"""
Creates class BaseGeometry
"""


class BaseGeometry():
    """instance of class BaseGeometry"""
    def __init__(self):
        """initialize class"""
        pass

    def area(self):
        """ Public instance method area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Public instance method area """
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
