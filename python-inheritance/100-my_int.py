#!/usr/bin/python3
"""Module that defines the MyInt class."""


class MyInt(int):
    """Rebel integer that has == and != inverted."""

    def __eq__(self, other):
        """Return the result of != from int."""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Return the result of == from int."""
        return int.__eq__(self, other)
