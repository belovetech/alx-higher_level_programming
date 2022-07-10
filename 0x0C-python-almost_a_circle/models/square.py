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
        self.size = self.width

    def __str__(self):
        """Represents square string to the stdout"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)
