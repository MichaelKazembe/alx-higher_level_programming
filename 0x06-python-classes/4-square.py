#!/usr/bin/python3
""" creates class Square """


class Square:
    """ class Square """
    def __init__(self, size=0):
        """ class Square object """
        self.__size = size

    @property
    def size(self):
        """get size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ public instance method"""
        return self.__size ** 2
