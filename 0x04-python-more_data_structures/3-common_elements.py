#!/usr/bin/python3
""" Returns a set of common elements in two sets """


def common_elements(s1, s2):
    """ Returns common elements if two sets """

    return set(s1 & s2)
