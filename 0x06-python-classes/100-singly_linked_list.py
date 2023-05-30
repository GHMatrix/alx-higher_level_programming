#!/usr/bin/python3
"""
Defining a class Node
"""


class Node:
    """
    Represents a node of a singly linked list.

    This class defines a node with its data and next_node attributes.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new instance of the Node class.

        Parameters:
            data (int): The data value of the node.
            next_node (Node, optional): The next node in the
            linked list. Default is None.

        Error raised:
            TypeError: If the provided data is not an
            integer or next_node is not a Node object.
        """
        self.__data = None
        self.__next_node = None
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieve the data value of the node.

        Returns:
            int: The data value of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data value of the node.

        Parameters:
            value (int): The data value of the node.

        Error raised:
            TypeError: If the provided data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieve the next node in the linked list.

        Returns:
            Node: The next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node in the linked list.

        Parameters:
            value (Node): The next node in the linked list.

        Error raised:
            TypeError: If the provided next_node is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Represents a singly linked list.

    This class defines a linked list with its
    head attribute and related operations.
    """

    def __init__(self):
        """Initialize a new instance of the SinglyLinkedList class."""
        self.head = None

    def sorted_insert(self, value):
        """
        Insert a new Node into the correct sorted
        position in the list (increasing order).

        Parameters:
            value (int): The value to be inserted.

        Error raised:
            TypeError: If the provided value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("value must be an integer")

        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and value >= current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Return a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        output = ""
        current = self.head
        while current is not None:
            output += str(current.data) + "\n"
            current = current.next_node
        return output.strip()
