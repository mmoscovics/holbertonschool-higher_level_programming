#!/usr/bin/python3
""" Copy string and remove character at position n """


def remove_char_at(str, n):
    """ Copy string and remove character """

    strcp = ""

    for i in range(0, len(str)):
        if i is not n:
            strcp += str[i]
    return strcp
