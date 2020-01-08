#!/usr/bin/python3
""" Function that prints an integer with exception error message. """
from sys import stderr


def safe_print_integer_err(value):
    """ Prints an integer with exception error message. """

    try:
        print("{:d}".format(value))
        return True
    except Exception as ex:
        print("Exception: {}".format(ex), file=stderr)
        return False
