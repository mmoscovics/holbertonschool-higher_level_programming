#!/usr/bin/python3
""" Returns list with all values mutiplied by a number without using loops """


def mutiply_list_map(my_list=[], number=0):
    """ Returns lists with values multiplied """

    return list(map(lambda value: value * number, my_list))
