#!/usr/bin/python3
"""Module 0-add_integer.

Provides a function that adds two integers.
Floats are accepted and cast to integers first.
"""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Raises TypeError if a or b is not an integer or a float."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
