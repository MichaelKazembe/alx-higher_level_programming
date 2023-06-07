#!/usr/bin/python3
"""
101-lazy_matrix_mul.py

This module defines a matrix multiplication function
`lazy_matrix_mul(m_a, m_b)`.

"""


def lazy_matrix_mul(m_a, m_b):
    """
    Perform lazy matrix multiplication of two matrices.

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.

    Returns:
        list: The resulting matrix after multiplication.

    Raises:
        TypeError: If either `m_a` or `m_b` is not a list of lists.
        ValueError: If the dimensions of `m_a` and `m_b` are not
        compatible for multiplication.

    """

    # Check if m_a and m_b are lists
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a and m_b must be lists")

    # Check if m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a and m_b must be lists of lists")

    # Check if m_a and m_b are not empty
    if not m_a or not m_b:
        raise ValueError("m_a and m_b cannot be empty")

    # Check if the dimensions of m_a and m_b are compatible for multiplication
    if len(m_a[0]) != len(m_b):
        raise ValueError(f"shapes ({len(m_a)},{len(m_a[0])}) and ({len(m_b)},{len(m_b[0])}) not aligned: {len(m_a[0])} (dim 1) != {len(m_b)} (dim 0)")

    # Perform matrix multiplication
    result = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]

    return result
