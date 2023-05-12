#!/usr/bin/python3

"""
   Prints the alphabet in uppercase
   followed by a new line

"""


def print_upper_alpha():
    for upper_alpha in range(65, 91):
        print("{}".format(chr(upper_alpha)), end='')
