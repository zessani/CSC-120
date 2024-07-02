"""
    File: linkedlist_sort.py
    Author: Zayyan Essani
    Course: CSC 120, Spring 2024
    Purpose: This program writes a method for the linkedlist class
            that sorts the linkedlist in descending order of the _values
            attributes of the nodes.
"""

class LinkedList:
    def __init__(self):
        self._head = None
    
    # sort the nodes in the list
    def sort(self):
        """
        Sorts the LinkedList object in descending order of the
        ._value attribute.

        Parameters: self: the object itself

        Returns: None
        """
        sorted_list = LinkedList()  

        while self._head is not None:
            curr_element = self.remove() 
            curr_value = curr_element._value

            if sorted_list._head is None or \
                sorted_list._head._value <= curr_value:
                curr_element._next = sorted_list._head
                sorted_list._head = curr_element
            else:
                # find the correct position to insert the current element.
                prev = None
                current = sorted_list._head
                while current is not None and current._value > curr_value:
                    prev = current
                    current = current._next
                if prev is None:
                    sorted_list._head = curr_element
                else:
                    prev._next = curr_element
                curr_element._next = current

        # Copy sorted list back to the original list
        self._head = sorted_list._head
    
    # add a node to the head of the list
    def add(self, node):
        node._next = self._head
        self._head = node
        
    # remove a node from the head of the list and return the node
    def remove(self):
        assert self._head != None
        _node = self._head
        self._head = _node._next
        _node._next = None
        return _node
    
    # insert node2 after node1
    def insert(self, node1, node2):
        assert node1 != None
        node2._next = node1._next
        node1._next = node2
    
    def __str__(self):
        string = 'List[ '
        curr_node = self._head
        while curr_node != None:
            string += str(curr_node)
            curr_node = curr_node.next()
        string += ']'
        return string

class Node:
    def __init__(self, value):
        self._value = value
        self._next = None
    
    def __str__(self):
        return str(self._value) + "; "
    
    def value(self):
        return self._value
    
    def next(self):
        return self._next
    
def main():
    filename = input()
    file = open(filename, 'r')

    numbers = []
    for line in file:
        for num in line.split():
            numbers.append(int(num))
    file.close()
    linked_list = LinkedList()
    for num in numbers:
        linked_list.add(Node(num))

    linked_list.sort()
    print(linked_list)

main()