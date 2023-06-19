#!/usr/bin/python3
""" square.py """

from rectangle import Rectangle


class Square(Rectangle):
    """ Class Square that inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Class Square constructor """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter function for size """
        return self.width

    @size.setter
    def size(self, size):
        """ Setter function for size """
        self.width = size
        self.height = size

    def __str__(self):
        """ String representation of the square object """
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width
        )
