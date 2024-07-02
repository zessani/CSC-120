"""
    File: linked_list.py
    Author: Zayyan Essani
    Course: CSC 120, Spring 2024
    Purpose: This program contains two classes linked_list
            and Node classes. These are used in the program
            friends.py.
"""
class Node:
    """
    This class represents information about names and friends.

       The class defines the methods for defining the Node object,
    """
    def __init__(self, name):
        """
        This function initializes a Node object by 
        creating a linked list and initalizing ._next
        to None.
    
        Parameters: self: the object itself
                    name: string of name
    
        Returns: None 

        """
        self._name = name
        self._friends = LinkedList()
        self._next = None

class LinkedList:
    """
    This class represents information about data and
    friends. It uses the Node class

       The class defines the methods for defining the LinkedList object,
       chcecking if its empty, adding a person and sorting the list.
    """

    def __init__(self):
        """
        This function initializes a Linkedlist object by 
        initalizing the head.
    
        Parameters: self: the object itself   
        Returns: None 

        """
        self._head = None

    def add(self, new):
        new._next = self._head
        self._head = new

    def is_empty(self):
        return self._head == None

    def find(self, name):
        """
        This function finds the node linked to the 
        name
        Parameters: name to be found
    
        Returns: None

        """
        if not self._head:
            return None

        current = self._head

        while current:
            if current._name == name:
                return current
            current = current._next

        return None

    def print(self):
        current = self._head
        while current:
            print (current._name)
            current = current._next

    def rm_from_hd(self):
        """
        This function removes the first node from the linked list,
        updating the list's _head attribute, and returns the
        removed node. It raises an error if the method is 
        called on an empty list.

        Parameters: self: object itself
    
        Returns: the removed node

        """
        hd = self._head
        self._head = hd._next
        return hd

    def insert_after(self, node1, node2):
        # insert node2 after node1
        # source: long problem for sorting a linked lists
        temp = node1._next
        node1._next = node2
        node2._next = temp

    def sort(self):
        """
        This function sorts the linked list according
        to the names.

        Parameters: self: object itself
    
        Returns: sorted list

        """
        if not self._head:
            return None
        
        sorted_list = LinkedList()

        unsorted = self._head

        while unsorted:
            self.rm_from_hd()
            name_node = Node(unsorted._name)
            # if empty, add unsorted to sorted.
            if sorted_list.is_empty():
                sorted_list.add(name_node)
 
            elif sorted_list._head._name > unsorted._name:
                sorted_list.add(name_node)

            else:
                
                sorted = sorted_list._head

                while sorted:
                    if unsorted._name >= sorted._name:
                        # insert the removed node after the current node
                        if sorted._next == None or sorted._next._name > unsorted._name:
                            sorted_list.insert_after(sorted, name_node)

                    sorted = sorted._next

            unsorted = unsorted._next

        return sorted_list