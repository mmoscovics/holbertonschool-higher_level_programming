#!/usr/bin/python3
""" Function that appends a string at the end of a text file
Returns the number of characters added.
"""


def append_write(filename="", text=""):
    """ Appends a string at the end of a text file
    Returns number of characters added. """

    if filename is '':
        return
    with open(filename, "a+") as f:
        return f.write(text)
