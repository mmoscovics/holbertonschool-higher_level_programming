#!/usr/bin/python3
""" Prints string in uppercase followed by a new line """


def uppercase(str):
    """ Prints string in uppercase """

    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            ch = ord(i) - 32
        else:
            ch = ord(i)
        print("{}".format(chr(ch)), end="")
    print()
