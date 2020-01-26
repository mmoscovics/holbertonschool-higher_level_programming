#!/usr/bin/python3
""" Class Square that inherits from Rectangle. """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square that inherits from Rectangle. """

    def __init__(self, size, x=0, y=0, id=None):
        """ Class Constructor. """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ String representor.
        Returns a string that represents Square. """

        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """ Public method that updates class Square.
        Assigns an argument to each attribute. """

        argc = len(args)

        if argc <= 0:
            self.id = kwargs.get('id', self.id)
            self.size = kwargs.get('size', self.size)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)
        if argc > 0:
            self.id = (args[0])
        if argc > 1:
            self.size = args[1]
        if argc > 2:
            self.x = args[2]
        if argc > 3:
            self.y = args[3]

    @property
    def size(self):
        """ Public getter for size. """

        return self.width

    @size.setter
    def size(self, value):
        """ Public setter for size.
        Sets width and height to value. """

        self.width = value
        self.height = value
