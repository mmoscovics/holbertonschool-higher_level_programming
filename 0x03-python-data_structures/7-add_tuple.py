#!/usr/bin/python3
""" Adds 2 tuples """


def add_tuple(a=(), b=()):
    """ Adds 2 tuples """

    if len(a) is 0:
        a = (0, 0)
    elif len(a) is 1:
        a = (a[0], 0)
    if len(b) is 0:
        b = (0, 0)
    elif len(b) is 1:
        b = (b[0], 0)
    return tuple(map(lambda x, y: x + y, a, b))
