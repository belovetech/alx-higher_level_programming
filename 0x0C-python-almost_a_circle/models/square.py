#!/usr/bin/python3
"""Defines Square class that inherits from Rectangle class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines Square class with its attributes"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square objects/instances

        Args:
            size (int): size of the square
            x (int): horizontal coordinates
            y (int): vertical coordinates
            id (int): id of the instances
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size property getter: retrives the size of the square

        Returns:
            size (int): the size instance attributes

        size.setter: set the size of the square

        Args:
            value (int): inherit width and height from Rectangle as size
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Represents square string to the stdout"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)
