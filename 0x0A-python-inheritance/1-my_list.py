#!/usr/bin/python3
"""
A class MyList that inherits from list

"""


class MyList(list):
    """ class MyList """
    def print_sorted(self):
        """  prints the list, but sorted (ascending sort) """
        sorted_list = sorted(self)
        print(sorted_list)
