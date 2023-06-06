#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Add two integers.

    Args:
        a (int or float): First integer or float.
        b (int or float, optional): Second integer or float. Defaults to 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.

    Examples:
        >>> add_integer(3, 5)
        8

        # Rest of the examples...

    """

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
