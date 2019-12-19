#!/usr/bin/python3
""" Replaces or adds key/value in a dictionary """


def update_dictionary(a_dictionary, key, value):
    """ Updates dictionary """

    a_dictionary.update({key: value})
    return a_dictionary
