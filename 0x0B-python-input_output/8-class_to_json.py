#!/usr/bin/python3
"""
function that returns the dictionary description with
simple data structure (list, dictionary, string,
integer and boolean) for JSON serialization of an object

"""


def class_to_json(obj):
    """class class_to_json"""
    obj_attr = obj.__dict__
    json_dict = {}

    for key, value in obj_attr.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value

    return json_dict
