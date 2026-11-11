#!/usr/bin/python3
"""Module that defines a Square class with a private size attribute."""


class Square:
    """Class that defines a square by its size."""

    def __init__(self, size):
        """Initialize a square with a private size.

        Args:
            size: the size of the square (no validation yet).
        """
        self.__size = size
