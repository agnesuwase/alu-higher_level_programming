#!/usr/bin/python3
"""Module that defines the MyList class."""


class MyList(list):
    """List with a method that prints itself sorted."""

    def print_sorted(self):
        """Print the list in ascending order without changing it."""
        print(sorted(self))
