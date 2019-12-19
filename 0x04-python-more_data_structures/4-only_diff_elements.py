#!/usr/bin/python3
""" Returns set of all elements present in only one set """


def only_diff_elements(s1, s2):
    """ Returns elements present in only one set """

    return set(s1 ^ s2)
