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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts dictionary to JSON string representation

        Args:
            list_dictionaries (dict): List of dictionaries

        Returns:
            JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string representation of list_objs to a file.

        Args:
            list_objs (list): is a list of instances who inherits of Base
        """

        filename = cls.__name__ + ".json"

        with open(filename, "w", encoding="utf-8") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dict = [list.to_dictionary() for list in list_objs]
                file.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Converts JSON string to dictionary representation

        Args:
            json_string (dict): JSON string representation

        Returns:
            JSON string representation of json_string
        """
        if json_string is None or json_string == []:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Assign dictionary values to Instances

        Args:
            **dictionary (dict): list of dictionary

        Returns:
            an instance with all attributes already set
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_values = cls(1, 1)
            else:
                new_values = cls(1)
            new_values.update(**dictionary)
            return new_values
