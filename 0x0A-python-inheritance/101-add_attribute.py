#!/usr/bin/python3
"""
a function that adds a new attribute to an object if it’s possible

"""


def add_attribute(obj, attr, value):
    """Add a new attribute to an object if possible"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
