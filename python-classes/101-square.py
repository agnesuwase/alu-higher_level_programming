#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Square with a size and a position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square.

        Args:
            size (int): the size of the square.
            position (tuple): the position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get or set the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get or set the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) is not tuple or len(value) != 2 or
                not all(type(n) is int for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def __str__(self):
        """Return the square drawn with the # character."""
        if self.__size == 0:
            return ""
        lines = [""] * self.__position[1]
        for _ in range(self.__size):
            lines.append(" " * self.__position[0] + "#" * self.__size)
        return "\n".join(lines)

    def my_print(self):
        """Print the square with the # character."""
        print(self)
