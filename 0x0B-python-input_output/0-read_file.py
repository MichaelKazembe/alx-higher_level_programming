#!/usr/bin/python3

"""
a function that reads a text file (UTF8) and prints it to stdout

"""


def read_file(filename=""):
    """function read_file"""
    with open(filename, encoding="UTF-8") as file:
        file_contents = file.read()
        print(file_contents)
