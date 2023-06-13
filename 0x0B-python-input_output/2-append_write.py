#!/usr/bin/python3

"""
a function that appends a string at the end of
a text file (UTF8) and returns the number of
characters added:

"""


def append_write(filename="", text=""):
    """function append_write"""
    with open(filename, "a", encoding="UTF-8") as file:
        file.write(text)
        return len(text)
