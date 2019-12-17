#!/usr/bin/python3
""" Returns an element from a list at index """


def element_at(my_list, idx):
    """ Returns an element """

    if idx < 0:
        return None
    if idx > len(my_list):
        return None
    for i in my_list:
        if i is idx:
            return my_list[i]
