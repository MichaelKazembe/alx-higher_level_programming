#!/usr/bin/python3

"""
A function that writes an Object to
a text file, using a JSON representation:
"""

import json


def save_to_json_file(my_obj, filename):
    """function save_to_json_file"""
    with open(filename, "w", encoding="UTF-8") as file:
        json.dump(my_obj, file)
