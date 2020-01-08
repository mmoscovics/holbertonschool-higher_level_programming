#!/usr/bin/python3
""" Function that executes a function safely. """
from sys import stderr


def safe_function(fct, *args):
    """ Executes a function safely. """

    try:
        result = fct(*args)
        return result
    except Exception as ex:
        print("Exception: {}".format(ex), file=stderr)
        return None
