#!/usr/bin/python3
""" Class Rectangle that defines a rectangle. """


class Rectangle:
    """ Class Rectangle. """

    def __init__(self, width=0, height=0):
        """ Instantiation with optional width and height. """

        self.width = width
        self.height = height

    def area(self):
        """ Method that returns the rectangle area. """

        return self.width * self.height

    def perimeter(self):
        """ Method that returns the rectangle perimeter. """

        if self.width is 0 or self.height is 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    @property
    def width(self):
        """ Getter for attribute width.
        Returns width after setter.
        """

        return self.__width

    @width.setter
    def width(self, value):
        """ Sets width to value after checks. """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for attribute height.
        Returns height after setter.
        """

        return self.__height

    @height.setter
    def height(self, value):
        """ Sets height to value after checks. """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
