#!/usr/bin/python3
"""Module 2-matrix_divided.

Provides a function that divides all elements of a matrix.
The matrix must be a list of lists of integers or floats.
Results are rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """Return a new matrix with every element divided by div.

    Raises TypeError or ZeroDivisionError on invalid input."""
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(msg)
    for row in matrix:
        if not isinstance(row, list) or row == []:
            raise TypeError(msg)
        for item in row:
            if type(item) not in (int, float):
                raise TypeError(msg)
    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in row] for row in matrix]
