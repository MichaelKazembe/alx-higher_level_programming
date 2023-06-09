#!/usr/bin/python3

"""
A module that Prints "My name is <first name> <last name>".

"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>".

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to an empty string.

    Raises:
        TypeError: If first_name is not a string or last_name is not a string.

    Examples:
        >>> say_my_name("Peter", "Pan
        My name is John Doe

        >>> say_my_name("Michael
        My name is Michael

        >>> say_my_name(123, "Smith")
        Traceback (most recent call last):
            ...
        TypeError: first_name must be a string

        >>> say_my_name("Alice", 456)
        Traceback (most recent call last):
            ...
        TypeError: last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
