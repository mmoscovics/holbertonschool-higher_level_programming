#!/usr/bin/python3
""" Class Square that defines a square. """


class Square:
    """ Class Square. """

    def __init__(self, size=0):
        """ Initialize size of Class Square, checks size variable. """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Defines area of Class Square. """

        return self.__size**2
