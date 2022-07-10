#!/usr/bin/python3
"""Representation of a Base class with its attributes"""

import json


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
            type(self).__nb_objects += 1
            self.id = self.__nb_objects

    def to_json_string(list_dictionaries):
        """Converts dictionary to JSON string representation

        Args:
            list_dictionaries (dict): List of dictionaries

        Returns:
            JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
