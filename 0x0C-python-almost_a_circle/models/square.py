#!/usr/bin/python3
"""
Module containing the Square class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class representing a square, a specific type of rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.

        Args:
            size (int): Size of the square (width and height).
            x (int, optional): X coordinate of the square's position.
            y (int, optional): Y coordinate of the square's position.
            id (int, optional): Unique ID of the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Get or set the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("Size must be an integer.")
        if value <= 0:
            raise ValueError("Size must be > 0.")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the attributes of the square.

        Args:
            *args: Variable length argument list.
                - If args is not empty:
                    - args[0] (int, optional): New ID of the square.
                    - args[1] (int, optional): New size of the square.
                    - args[2] (int, optional): New x coordinate of the square's position.
                    - args[3] (int, optional): New y coordinate of the square's position.
                - If args is empty:
                    - kwargs (dict): Key-value pairs of attributes to update.
        """
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i, value in enumerate(args):
                setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of the square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

