#!/usr/bin/python3
""" Class Student that defines a student by
Public instance attributes:
first name, last name, age.
"""


class Student:
    """ Class Student. """

    def __init__(self, first_name, last_name, age):
        """ Instantiate attributes
        first_name, last_name, age. """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student. """

        if type(attrs) is list and all([type(i) is str for i in attrs]):
            return {k: v for k, v in vars(self).items() if k in attrs}
        return vars(self)

    def reload_from_json(self, json):
        """ Replaces all attributes of the Student instance. """

        for key, value in json.items():
            setattr(self, key, value)
