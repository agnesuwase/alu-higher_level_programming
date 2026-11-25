#!/usr/bin/python3
"""Defines a class Square that can be compared by area."""


class Square:
    """Square with a size, comparable by area."""

    def __init__(self, size=0):
        """Initialize a Square.

        Args:
            size (int or float): the size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Get or set the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) not in (int, float):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def __eq__(self, other):
        """Return True if both areas are equal."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Return True if areas are different."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Return True if this area is smaller."""
        return self.area() < other.area()

    def __le__(self, other):
        """Return True if this area is smaller or equal."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Return True if this area is bigger."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Return True if this area is bigger or equal."""
        return self.area() >= other.area()
