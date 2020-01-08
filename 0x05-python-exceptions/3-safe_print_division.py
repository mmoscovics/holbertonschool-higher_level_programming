#!/usr/bin/python3
""" Function that divides 2 integers and prints result. """


def safe_print_division(a, b):
    """ Prints quotient of 2 integers. """

    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
