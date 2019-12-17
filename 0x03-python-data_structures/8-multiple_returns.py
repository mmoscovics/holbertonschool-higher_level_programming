#!/usr/bin/python3
""" Returns a tuple with the length of a string and its first character """


def multiple_returns(sentence):
    """ Returns a tuple """

    if sentence is '':
        return (len(sentence), None)
    return (len(sentence), sentence[0])
