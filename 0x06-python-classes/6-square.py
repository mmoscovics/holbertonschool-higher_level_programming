#!/usr/bin/python3
""" Class Square that defines a square. """


class Square:
    """ Class Square. """

    def __init__(self, size=0, position=(0, 0)):
        """ Initialize size of Class Square. """

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ Gets and returns position after setter. """

        return self.__position

    @position.setter
    def position(self, value):
        """ Sets position to value after exception checks. """

        if type(value) is not tuple or len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int and value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) is not int and value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """ Prints the square with character #. """

        if self.size is 0:
            print()
            return
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print((" " * self.__position[0]) + ("#" * self.__size))
