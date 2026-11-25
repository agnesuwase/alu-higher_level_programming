#!/usr/bin/python3
"""Module 4-print_square.

Provides a function that prints a square with the character #.
The size must be a non-negative integer.
"""


def print_square(size):
    """Print a square of size lines made of the character #.

    Raises TypeError or ValueError if size is invalid."""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
