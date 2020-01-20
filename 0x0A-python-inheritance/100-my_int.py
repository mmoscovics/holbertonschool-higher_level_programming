#!/usr/bin/python3
""" Class MyInt that inherits from int. """


class MyInt(int):
    """ Class MyInt that inherits from int
    inverts eq and ne operators. """

    def __eq__(self, value):
        """ Returns ne value. """

        return super().__ne__(value)

    def __ne__(self, value):
        """ Returns eq value. """

        return super().__eq__(value)
