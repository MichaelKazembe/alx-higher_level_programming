#!/usr/bin/python3
""" rectangle.py """

from models.base import Base


class Rectangle(Base):
    """ Class Rectangle that inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Class Rectangle constructor """
        self.__width = None
        self.__height = None
        self.__x = None
        self.__y = None
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Getter function for width """
        return self.__width

    @width.setter
    def width(self, width):
        """ Setter function for width """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ Getter function for height """
        return self.__height

    @height.setter
    def height(self, height):
        """ Setter function for height """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ Getter function for x """
        return self.__x

    @x.setter
    def x(self, x):
        """ Setter function for x """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ Getter function for y """
        return self.__y

    @y.setter
    def y(self, y):
        """ Setter function for y """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ Public method that returns the area of the rectangle """
        return self.width * self.height

    def display(self):
        """ Public method that prints the rectangle using '#' characters """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """ String representation of the rectangle object """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id,
            self.x,
            self.y,
            self.width,
            self.height
        ))

    def update(self, *args, **kwargs):
        """ Public method to update attributes of the rectangle """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Public method that returns the dictionary
        representation of a Rectangle
        """
        return {"id": self.id, "width": self.width,
                "height": self.height,
                "x": self.x, "y": self.y}
