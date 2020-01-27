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

        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
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

        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Class method that returns an instance with all attributes set. """

        if cls.__name__ is "Rectangle":
            obj = cls(1, 1)
        elif cls.__name__ is "Square":
            obj = cls(1)
        else:
            return None
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """ Class method thar returns a list of instances. """

        with open(cls.__name__ + ".json", "r+") as file:
            obj = cls.from_json_string(file.read())
        return [cls.create(**dict) for dict in obj]
