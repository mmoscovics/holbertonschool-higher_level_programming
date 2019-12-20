#!/usr/bin/python3
""" Deletes keys with a specific value in a dictionary """


def complex_delete(a_dictionary, value):
    """ Deletes keys by value """

    for key, val in list(a_dictionary.items()):
        if val is value:
            del a_dictionary[key]
    return a_dictionary
