#!/usr/bin/python3
""" Function that writes to a text file
Returns the number of characters written.
"""


def write_file(filename="", text=""):
    """ Writes a string to a text file
    Returns number of characters written. """

    if filename is '':
        return
    with open(filename, "w+") as f:
        return f.write(text)
