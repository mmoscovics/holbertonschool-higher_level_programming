#!/usr/bin/python3
""" Replace element of a list at index """


def replace_in_list(my_list, idx, element):
    """ Replace element at index """

    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
