#!/usr/bin/python3
""" Class Node the defines a node of a singly linked list. """


class Node:
    """ Class Node. """

    def __init__(self, data, next_node=None):
        """ Instantiate Class with data, and next_node. """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Gets and returns data after setter. """

        return self.__data

    @data.setter
    def data(self, value):
        """ Sets data with value after exception handling. """

        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Gets and returns next_node after setter. """

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Sets next_node with value after exception handling. """

        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """ Class SinglyLinkedList that defines a singly linked list. """

    def __init__(self):
        """ Instantiate head. """

        self.__head = None

    def __str__(self):
        """ Makes a string representation to be printed. """

        string = ""
        pos = self.__head
        if pos is None:
            string = ""
            return string
        while pos is not None :
            string += str(pos.data) + '\n'
            pos = pos.next_node
        return string[:-1]

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list.
        """

        if self.__head is None:
            self.__head = Node(value, None)
        node = self.__head
        pos = None
        while node is not None and node.data <= value:
            pos = node
            node = node.next_node
        node = Node(value, node)
        if pos is not None:
            pos.next_node = node
        self.__head = node
