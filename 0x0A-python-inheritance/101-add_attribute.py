#!/usr/bin/python3
"""
a function that adds a new attribute to an object if it’s possible

"""


def add_attribute(obj, attr_name, attr_value):
    """Add a new attribute to an object if possible"""
    if hasattr(obj, attr_name):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr_name, attr_value)
