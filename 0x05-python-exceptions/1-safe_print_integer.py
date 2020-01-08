#!/usr/bin/python3
""" Function that prints an integer with .format """


def safe_print_integer(value):
    """ Prints integer with .format """

    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
