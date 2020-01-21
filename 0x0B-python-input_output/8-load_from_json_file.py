#!/usr/bin/python3
""" Function that creates an Object from a "JSON file". """
import json


def load_from_json_file(filename):
    """ Creates an obj from JSON file. """

    with open(filename, 'r') as f:
        return json.load(f)
