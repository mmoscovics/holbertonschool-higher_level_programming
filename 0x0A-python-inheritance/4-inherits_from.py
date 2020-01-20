#!/usr/bin/python3
""" Function that returns True if the object is an instance of a class
that inherited from the specified class; otherwise False.
"""


def inherits_from(obj, a_class):
    """ Returns true or false for subclass. """

    return issubclass(type(obj), a_class) and not type(obj) is a_class
