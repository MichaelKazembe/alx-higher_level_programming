#!/usr/bin/python3
""" Int Class"""


class MyInt(int):
    """class utilizing int class"""
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        """reverses equals to not equals """
        if int.__ne__(self, other):
            return True
        else:
            return False

    def __ne__(self, other):
        """reverses not equals to equals"""
        if int.__eq__(self, other):
            return True
        else:
            return False
