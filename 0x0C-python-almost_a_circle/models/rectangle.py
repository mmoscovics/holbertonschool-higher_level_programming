#!/usr/bin/python3
""" Class Rectangle that inherits from Base. """
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle that inherits from Base. """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Class constructor. """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def area(self):
        """ Public method for area.
        Returns area value of Rectangle. """

        return self.width * self.height

    def display(self):
        """ Public method that prints in stdout the Rectangle.
        Using character #. """

        for y_iter in range(self.y):
            print()
        for height_iter in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """ String representor.
        Returns a string that represents Rectangle. """

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args):
        """ Public method that updates class Rectangle.
        Assigns an argument to each attribute. """

        argc = len(args)

        if argc > 0:
            super().__init__(args[0])
        if argc > 1:
            self.width = args[1]
        if argc > 2:
            self.height = args[2]
        if argc > 3:
            self.x = args[3]
        if argc > 4:
            self.y = args[4]

    @property
    def width(self):
        """ Public getter for width.
        Returns width. """

        return self.__width

    @width.setter
    def width(self, value):
        """ Public setter for width.
        Sets width to value.
        Checks value. """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Public getter for height.
        Returns height. """

        return self.__height

    @height.setter
    def height(self, value):
        """ Public setter for height.
        Sets height to value.
        Checks value. """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 1:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Public getter for x.
        Returns x. """

        return self.__x

    @x.setter
    def x(self, value):
        """ Public setter for x.
        Sets x to value.
        Checks value. """

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Public getter for y.
        Returns y. """

        return self.__y

    @y.setter
    def y(self, value):
        """ Public setter for y.
        Sets y to value.
        Checks value. """

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
