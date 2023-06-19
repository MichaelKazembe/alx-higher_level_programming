#!/usr/bin/python3
""" base.py """

import os
import json
import csv


class Base:
    """ Base class for managing id attribute """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Convert list of dictionaries to JSON string """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ Convert JSON string to list of dictionaries """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @staticmethod
    def to_csv_string(list_objects):
        """ Convert list of objects to CSV string """
        if list_objects is None or len(list_objects) == 0:
            return ""
        class_name = list_objects[0].__class__.__name__
        field_names = Base.get_field_names(class_name)
        rows = [field_names]
        for obj in list_objects:
            obj_data = [str(getattr(obj, field_name))
                        for field_name in field_names]
            rows.append(obj_data)
        csv_string = ""
        for row in rows:
            csv_string += ",".join(row) + "\n"
        return csv_string

    @staticmethod
    def from_csv_string(csv_string):
        """ Convert CSV string to list of dictionaries """
        if csv_string is None or len(csv_string) == 0:
            return []
        rows = csv_string.strip().split("\n")
        field_names = rows[0].split(",")
        dictionaries = []
        for row in rows[1:]:
            values = row.split(",")
            dictionary = {field_name: value
                          for field_name, value in zip(field_names, values)}
            dictionaries.append(dictionary)
        return dictionaries

    @classmethod
    def create(cls, **dictionary):
        """ Create instance with attributes from dictionary """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            dummy_instance = cls()
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """ Load instances from file """
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, "r") as file:
            json_string = file.read()
            dictionaries = cls.from_json_string(json_string)
            instances = [cls.create(**dictionary)
                         for dictionary in dictionaries]
            return instances

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save instances to file as JSON """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None or len(list_objs) == 0:
                file.write("[]")
            else:
                dictionaries = [obj.to_dictionary() for obj in list_objs]
                json_string = cls.to_json_string(dictionaries)
                file.write(json_string)

    @classmethod
    def load_from_file_csv(cls):
        """ Load instances from CSV file """
        filename = cls.__name__ + ".csv"
        if not os.path.exists(filename):
            return []

    ...

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Save instances to file as CSV """
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as file:
            if list_objs is None or len(list_objs) == 0:
                file.write("")
            else:
                csv_string = cls.to_csv_string(list_objs)
                file.write(csv_string)
