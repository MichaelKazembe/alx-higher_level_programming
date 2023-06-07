#!/usr/bin/python3

"""
The `5-text_indentation` module
===============================

This module defines a function `text_indentation(text)`
that prints a text with 2 new lines after each of the
characters '.', '?', and ':'.

"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':' character.

    Parameters:
    -----------
    text : str
        The text to be processed.

    Raises:
    -------
    TypeError
        If `text` is not a string.

    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""
    punctuation_chars = ['.', '?', ':']
    for char in text:
        new_text += char
        if char in punctuation_chars:
            new_text += "\n\n"

    lines = new_text.splitlines()
    stripped_lines = [line.strip() for line in lines]
    print('\n'.join(stripped_lines))
