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

    @property
    def width(self):
        """ Public getter for width.
        Returns width. """

        return self.__width

    @width.setter
    def width(self, value):
        """ Public setter for width.
        Sets width to value. """

        self.__width = value

    @property
    def height(self):
        """ Public getter for height.
        Returns height. """

        return self.__height

    @height.setter
    def height(self, value):
        """ Public setter for height.
        Sets height to value. """

        self.__height = value

    @property
    def x(self):
        """ Public getter for x.
        Returns x. """

        return self.__x

    @x.setter
    def x(self, value):
        """ Public setter for x.
        Sets x to value. """

        self.__x = value

    @property
    def y(self):
        """ Public getter for y.
        Returns y. """

        return self.__y

    @y.setter
    def y(self, value):
        """ Public setter for y.
        Sets y to value. """

        self.__y = value
