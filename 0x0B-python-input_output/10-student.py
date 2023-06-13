#!/usr/bin/python3

"""
class Student that defines a student by

"""


class Student():
    """Class student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of the student instance"""
        student_attr = self.__dict__
        student_dict = {}

        if attrs is None:
            attrs = student_attr.keys()

        for key, value in student_attr.items():
            if key in attrs:
                student_dict[key] = value

        return student_dict
