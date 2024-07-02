"""
    File: friends.py
    Author: Zayyan Essani
    Course: CSC 120, Spring 2024
    Purpose: This program uses classes from linked_list.py,
            it analyzes a file, records names and finds mutual
            friends between two people.
"""

from linked_list import *

def read_file():
    """
    Reads the input file, and constructs a linked list
    of names and their friends.

    Parameters: None
    Returns:
    name_list: A linked list containing nodes representing
            names and their associated friends.
    """
    filename = input('Input file: ')
    file = open(filename, 'r')

    lines = file.readlines()
    name_list = LinkedList()

    for line in lines:

        friends = line.strip().split(' ')

        name1_friend = friends[0]
        name2_friend = friends[1]

        node1_friend = name_list.find(name1_friend)
        node2_friend = name_list.find(name2_friend)

        if not node1_friend:
            node1_friend = Node(name1_friend)
            name_list.add(node1_friend)

        if not node2_friend:
            node2_friend = Node(name2_friend)
            name_list.add(node2_friend)

        node1_friend._friends.add(Node(name2_friend))
        node2_friend._friends.add(Node(name1_friend))

    file.close()
    return name_list


def common_friends(name_1_node, name_2_node):
    """
        This function finds and prints the common
        friends between two given nodes.

        Parameters: node1: node representing the first person
                    node2: node representing the second person.
    
        Returns: None

    """
    if not name_1_node or not name_2_node:
        return

    common_friends = LinkedList()
    name1 = name_1_node._friends._head
    while name1:

        name2 = name_2_node._friends._head

        while name2:        
            if name2._name == name1._name:
                common_friends.add(Node(name1._name))
            name2 = name2._next
        name1 = name1._next

    if not common_friends.is_empty():
        mutual_friends_sorted = common_friends.sort()

        print('Friends in common:')
        mutual_friends_sorted.print()


def get_names(name_list):
    """
        This function finds nodes in the linked list.

        Parameters: name_list:  A linked list containing nodes 
                    representing names and their associated friends.

    
        Returns: nodes representing the two names

    """
    name_1 = input('Name 1: ')
    name_2 = input('Name 2: ')

   
    name_1_node = name_list.find(name_1)
    name_2_node = name_list.find(name_2)
    if not name_1_node:
        print('ERROR: Unknown person ' + name_1)
    if not name_2_node:
        print('ERROR: Unknown person ' + name_2)

    return name_1_node, name_2_node


def main():
    
    name_list = read_file()
    node1, node2 = get_names(name_list)

    common_friends(node1, node2)


main()