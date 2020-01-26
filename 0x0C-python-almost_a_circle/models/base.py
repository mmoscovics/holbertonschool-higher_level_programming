#!/usr/bin/python3
""" First Class Base. """
import json


class Base:
    """ Class Base. """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor. """

        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Static method that returns the JSON string representation
        of the dictionary. """

        if list_dictionaries is None or len(list_dictionaries) <= 0:
            return "[]"
        return json.dumps(list_dictionaries)
