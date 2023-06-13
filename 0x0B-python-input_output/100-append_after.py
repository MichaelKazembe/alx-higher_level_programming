#!/usr/bin/python3

"""
a function that inserts a line of text to a file,
after each line containing a specific string

"""


def append_after(filename="", search_string="", new_string=""):
    """ function append_after """
    with open(filename, "r", encoding="UTF-8") as file:
        lines = file.readlines()

    with open(filename, "w", encoding="UTF-8") as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string + "\n")