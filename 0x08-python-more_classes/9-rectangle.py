#!/usr/bin/python3
""" Class Rectangle that defines a rectangle. """


class Rectangle:
    """ Class Rectangle.
    Counts number of instances.
    Defines what character is printed to represent rectangle.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Instantiation with optional width and height. """

        self.width = width
        self.height = height
        self.number_of_instances = 0
        Rectangle.number_of_instances += 1

    def area(self):
        """ Method that returns the rectangle area. """

        return self.width * self.height

    def perimeter(self):
        """ Method that returns the rectangle perimeter. """

        if self.width is 0 or self.height is 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Returns a string representation of the rectangle with character.
        If width or height is 0 returns empty string
        """

        string = ""

        if self.width is 0 or self.height is 0:
            return string
        for i in range(self.height):
            string += str(self.print_symbol) * self.width
            string += '\n'
        return string[:-1]

    def __repr__(self):
        """ Returns the string that represents the rectangle. """

        return "{}({}, {})".format(
            type(self).__name__,
            self.width, self.height)

    def __del__(self):
        """ Detect deletion of instance. """

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns the bigest rectangle based on area. """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ Returns a new Rectangle instance.
        Width and Height equal to size.
        """

        return cls(size, size)

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
