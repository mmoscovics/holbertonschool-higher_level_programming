#!/usr/bin/python3
""" Class Square that inherits from Rectangle. """

Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """ Class Square that inherits from Rectangle. """

    def __init__(self, size):
        """ Instantiation with size. """

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
