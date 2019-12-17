#!/usr/bin/python3
""" Returns an element from a list at index """


def element_at(my_list, idx):
    """ Returns an element """

    if idx < 0:
        return None
    elif idx >= len(my_list):
        return None
    else:
        return my_list(idx)
