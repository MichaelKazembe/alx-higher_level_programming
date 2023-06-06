#!/usr/bin/python3

"""
A function that divides all elements of a matrix.

"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number.

    Parameters:
    matrix (list of lists): The matrix to be divided. Each
    element of the matrix should be an integer or float.
    div (int or float): The number to divide the matrix elements by.

    Returns:
    list of lists: A new matrix where all elements are divided by the
    given number, rounded to 2 decimal places.

    Raises:
    TypeError:
        - If the matrix parameter is not a matrix
          (list of lists) of integers/floats.
        - If each row of the matrix does not have
           the same size.
        - If the div parameter is not a number (integer
          or float).
    ZeroDivisionError: If div is equal to 0.
    """

    ''' Validate matrix parameter '''
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    ''' Validate matrix rows size '''
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    ''' Validate div parameter '''
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    ''' Validate div is not equal to 0 '''
    if div == 0:
        raise ZeroDivisionError("division by zero")

    ''' Perform matrix division and rounding '''
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return new_matrix
