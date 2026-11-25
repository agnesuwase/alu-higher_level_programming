#!/usr/bin/python3
"""Module 100-matrix_mul.

Provides a function that multiplies 2 matrices.
Both matrices must be lists of lists of integers or floats.
"""


def matrix_mul(m_a, m_b):
    """Return the product of the matrices m_a and m_b.

    Raises TypeError or ValueError if the input is invalid."""
    matrices = (("m_a", m_a), ("m_b", m_b))
    for name, mat in matrices:
        if not isinstance(mat, list):
            raise TypeError("{} must be a list".format(name))
    for name, mat in matrices:
        if not all(isinstance(row, list) for row in mat):
            raise TypeError("{} must be a list of lists".format(name))
    for name, mat in matrices:
        if all(len(row) == 0 for row in mat):
            raise ValueError("{} can't be empty".format(name))
    for name, mat in matrices:
        for row in mat:
            for item in row:
                if type(item) not in (int, float):
                    raise TypeError(
                        "{} should contain only integers or floats"
                        .format(name))
    for name, mat in matrices:
        if any(len(row) != len(mat[0]) for row in mat):
            raise TypeError(
                "each row of {} must be of the same size".format(name))
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result = []
    for row in m_a:
        new_row = []
        for col in range(len(m_b[0])):
            total = 0
            for k in range(len(m_b)):
                total += row[k] * m_b[k][col]
            new_row.append(total)
        result.append(new_row)
    return result
