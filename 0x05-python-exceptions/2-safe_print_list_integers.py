#!/usr/bin/python3
""" Function that prints the first x elements of a list and only integers. """


def safe_print_list_integers(my_list=[], x=0):
    """ Prints first x elements of a list and only integers. """

    counter = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            counter += 1
        except (ValueError, TypeError):
            pass
    print()
    return counter
