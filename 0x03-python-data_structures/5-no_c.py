#!/usr/bin/python3
""" Removes all caharacters c and C from a string """


def no_c(my_string):
    """ Removes characters c and C """

    return my_string.translate({ord(i): None for i in 'cC'})
