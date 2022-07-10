#!/usr/bin/python3
"""Representation of a Base class with its attributes"""


class Base:
    """Define a class Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """A class with private class attributes.
        def __init__: initialize class Base

        Args:
            id (int): id of an instance of class Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
