#!/usr/bin/python3

"""
a function that inserts a line of text to a file,
after each line containing a specific string

"""


def append_after(filename="", search_string="", new_string=""):
    """ function append_after """
    new_lines = []
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            new_lines += [line]
            if line.find(search_string) != -1:
                new_lines += [new_string]

    with open(filename, 'w', encoding="utf-8") as file:
        file.write("".join(new_lines))
