#!/usr/bin/python3
""" Function that prints x elements of a list with exception handling. """


def safe_print_list(my_list=[], x=0):
    """ Prints x elements of a list with exception handling. """

    for i in range(0, x):
        try:
            print(my_list[i], end="")
        except:
            print()
            return i
    print()
    return x
