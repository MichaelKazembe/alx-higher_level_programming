#!/usr/bin/python3
""" square.py """

from models.rectangle import Rectangle


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


    def update(self, *args, **kwargs):
        """ Public method to update attributes of the rectangle """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
