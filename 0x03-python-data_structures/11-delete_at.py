#!/usr/bin/python3
""" Deletes item at index of a list """


def delete_at(my_list=[], idx=0):
    """ Deletes item of a list """

    if idx < 0 or idx >= len(my_list):
        return None
    del my_list[idx]
    return my_list
