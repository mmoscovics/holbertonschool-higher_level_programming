#!/usr/bin/python3
""" Replaces an element in a list at index without modifying the original """


def new_in_list(my_list, idx, element):
    """ Replaces element in a copy of a list at index """

    new_list = my_list.copy()

    if idx < 0:
        return my_list
    if idx > len(my_list):
        return my_list
    for i in my_list:
        if i is idx:
            new_list[i] = element
            return new_list
