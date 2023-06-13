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

    def to_json(self):
        """Retrieves a dictionary representation of the student instance"""
        student_attr = self.__dict__
        student_dict = {}

        for key, value in student_attr.items():
            if isinstance(value, (list, dict, str, int, bool)):
                student_dict[key] = value

        return student_dict
