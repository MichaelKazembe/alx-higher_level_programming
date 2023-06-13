#!/usr/bin/python3

"""
a function that returns an object (Python data structure)
represented by a JSON string:

"""

import json


def from_json_string(my_str):
    """function from_json_string"""
    json_string = json.loads(my_str)
    return json_string
