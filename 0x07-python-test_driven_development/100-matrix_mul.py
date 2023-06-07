#!/usr/bin/python3
"""
Module for matrix multiplication.
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
        m_a (list): First matrix represented as a list of lists.
        m_b (list): Second matrix represented as a list of lists.

    Raises:
        TypeError: If m_a or m_b is not a list or not a list of lists.
        ValueError: If m_a or m_b is empty.
        TypeError: If an element in m_a or m_b is not an integer or a float.
        TypeError: If m_a or m_b is not a rectangle (rows of different sizes).
        ValueError: If m_a and m_b cannot be multiplied.

    Returns:
        list: The resulting matrix of the multiplication.
    """

    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")

    if m_a == [] or m_b == [[]]:
        raise ValueError("m_a can't be empty or m_b can't be empty")

    if any(not all(isinstance(num, (int, float)) for num in row) for row in m_a) or \
            any(not all(isinstance(num, (int, float)) for num in row) for row in m_b):
        raise TypeError("m_a should contain only integers or floats or "
                        "m_b should contain only integers or floats")

    if any(len(row) != len(m_a[0]) for row in m_a) or any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result


if __name__ == "__main__":
    # Test the matrix_mul function here
    pass

