#!/usr/bin/python3

"""
class Student that defines a student by

"""


class Student:
    """Class student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of the student instance"""
        student_dict = {}

        if attrs is None:
            attrs = self.__dict__.keys()

        for key, value in self.__dict__.items():
            if key in attrs:
                student_dict[key] = value

        return student_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
