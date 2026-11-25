#!/usr/bin/python3
"""Module defining the Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square.

        Args:
            size (int): size of the square.
            x (int): x offset.
            y (int): y offset.
            id (int): id of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get or set the size."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update the attributes of the square.

        Args:
            *args: id, size, x, y in this order.
            **kwargs: key/value pairs of attributes.
        """
        keys = ["id", "size", "x", "y"]
        if args and len(args) > 0:
            for key, value in zip(keys, args):
                setattr(self, key, value)
        else:
            for key, value in kwargs.items():
                if key in keys:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the square."""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
