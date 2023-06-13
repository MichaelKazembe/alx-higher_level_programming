#!/usr/bin/python3

"""
a function that creates an Object from a “JSON file”:
"""

import json


def load_from_json_file(filename):
    """function load_from_json_file"""
    with open(filename, "r", encoding="UTF-8") as file:
        file_contents = file.read()
        return json.loads(file_contents)
