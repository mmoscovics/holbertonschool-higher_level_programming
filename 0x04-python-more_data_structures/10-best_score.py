#!/usr/bin/python3
""" Return key with biggest integer value """


def best_score(a_d):
    """ Returns key with biggest value """

    if a_d is None:
        return
    for key, value in a_d.items():
        if value is max(a_d.values()):
            return key
