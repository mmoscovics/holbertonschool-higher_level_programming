#!/usr/bin/python3
""" Class Square that defines a square. """


class Square:
    """ Class Square. """

    def __init__(self, size=0):
        """ Initialize size of Class Square. """

        self.size = size

    def area(self):
        """ Defines area of Class Square. """

        return self.__size ** 2

    @property
    def size(self):
        """ Gets and returns size after setter. """

        return self.__size

    @size.setter
    def size(self, value):
        """ Sets size to value after exception checks. """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """ Prints the square with character #. """

        if self.size is 0:
            print()
        for i in range(self.size):
            print("#" * self.size)
