#!/usr/bin/env python3

"""

This module defines a function `text_indentation(text)`
that prints a text with 2 new lines after each '.', '?',
and ':' character.

"""


def text_indentation(text):
    """
    Prints the text with 2 new lines after each '.', '?', and ':' character.

    Args:
        text (str): The input text.

    Returns:
        None
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
