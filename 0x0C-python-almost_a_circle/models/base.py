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

    @classmethod
    def save_to_file(cls,list_objs):
        """ Class method that writes the JSON string rep to a file. """

        if list_objs is None:
            list_objs = []
        list_objs = [obj.to_dictionary() for obj in list_objs]
        list_objs = cls.to_json_string(list_objs)
        with open(cls.__name__ + ".json", "w+") as file:
            file.write(list_objs)

    @staticmethod
    def from_json_string(json_string):
        """ Static method that returns the list of the JSON string rep. """

        if json_string is None or len(json_string) <= 0:
            return []
        return json.loads(json_string)
