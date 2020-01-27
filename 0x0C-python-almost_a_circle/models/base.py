#!/usr/bin/python3
""" First Class Base. """
import json
from os.path import exists
import csv


class Base:
    """ Class Base. """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor. """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Static method that returns the JSON string representation
        of the dictionary. """

        ld = list_dictionaries
        return "[]" if ld is None or not ld else json.dumps(ld)

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

        if not exists(cls.__name__ + ".json"):
            return []
        with open(cls.__name__ + ".json", "r+") as file:
            obj = cls.from_json_string(file.read())
        return [cls.create(**inst) for inst in obj]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Class method that serializes in CSV. """

        if list_objs is None:
            list_objs =[]
        if cls.__name__ is "Rectangle":
            attributes = ("id", "width", "height", "x", "y")
        elif cls.__name__ is "Square":
            attributes = ("id", "size", "x", "y")
        else:
            return
        list_objs = ([getattr(obj, attr) for attr in attributes]
                     for obj in list_objs)
        with open(cls.__name__ + ".csv", "w+", newline='') as file:
            write_obj = csv.writer(file)
            for row in list_objs:
                write_obj.writerow(row)

    @classmethod
    def load_to_file_csv(cls):
        """ Class method that deserializes in CSV. """
