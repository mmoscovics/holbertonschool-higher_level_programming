#!/usr/bin/python3
""" Prints dictionary by ordered keys """


def print_sorted_dictionary(a_dict):
    """ Prints sorted dictionary """

    for key in sorted(a_dict):
        print("{}: {}".format(key, a_dict[key]))
