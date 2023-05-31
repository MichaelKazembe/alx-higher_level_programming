#!/usr/bin/python3
"""
import math class magic class
"""
import math
""" Create class"""


class MagicClass:
    """Magic class from given bytecode output"""

    def __init__(self, radius=0):
        """initialize radius object"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        """returns area of circle"""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """returns circumference of circle"""
        return 2 * math.pi * self._MagicClass__radius
