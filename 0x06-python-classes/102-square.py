#!/usr/bin/python3
""" creates class Square """


class Square:
    """ class Square """

    def __init__(self, size=0):
        """
        Initialize Square object.

        """
        self.size = size

    @property
    def size(self):
        """ Get size of square """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Compare if two squares are equal based on their areas.

        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        Compare if two squares are not equal.

        """
        return not self.__eq__(other)

    def __gt__(self, other):
        """

        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """

        Args:
            other (Square): The other square to compare.

        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False

    def __lt__(self, other):
        """
        Compare if area of the current square is less than other square.

        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """
        Compare if the area of the current square is less than or equal

        Args:
            other (Square): The other square to compare.
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return False
