"""
    File: fake_news.py
    Author: Zayyan Essani
    Course: CSC 120, Spring 2024
    Purpose: This program analyzes data about fake news articles
            and identifies what they commonly focus on. It uses two
            classes, Node, which represents individual words along 
            with their counts, and a class which manages a linked list.
            The program reads an input file, cleans the title and sorts
            the words based on their counts.
"""

import csv
import string

class Node:
    """
    This class represents information about a word.

       The class defines the methods for defining the Node object,
       and the methods of returning the word, count and incrementing
       the counter. It also has a function to return it.
    """
    def __init__(self, word):
        """
        This function initializes a Node object by setting
        the count to one and _next to none.
    
        Parameters: self: the object itself
                    word: string of word
    
        Returns: None 

        """
        self._word = word
        self._count = 1
        self._next = None

    def word(self):
        return self._word

    def count(self):
        return self._count

    def next(self):
        return self._next

    def set_next(self, target):
        self._next = target

    def incr(self):
        self._count += 1

    def __str__(self):
        return "{} : {}".format(self._word, self._count)
    

class LinkedList:
    """
    This class represents a linked list.

       The class defines the methods for defining the Linked List object,
       and the methods for updating the counters, sorting the list,
       getting the highest counter and returning/printing the
       object.
    """
    def __init__(self):
        """
        This function initializes a LinkedList object by setting
        the head of the list to none.
    
        Parameters: self: the object itself
    
        Returns: None 

        """
        self._head = None

    def is_empty(self):
        return self._head is None

    def head(self):
        return self._head

    def update_count(self, word):
        """
        This function increments the counter if the word
        is present in the list, otherwise, add a node
        for it.
    
        Parameters: word: a string of word
    
        Returns: None

        """
        current = self._head
        while current is not None:
            # increment counter if word is present
            if current.word() == word:
                current.incr()
                return
            current = current.next()
        # add a node if word is not present
        new_node = Node(word)
        new_node.set_next(self._head)
        self._head = new_node

    def rm_from_hd(self):
        """
        This function removes the first node from the linked list,
        updating the list's _head attribute, and returns the
        removed node. It raises an error if the method is 
        called on an empty list.

        Parameters: self: object itself
    
        Returns: the removed node

        """
        removed = self._head
        self._head = removed.next()
        removed.set_next(None)
        return removed

    def insert_after(self, node1, node2):
        # insert node2 after node1
        # source: long problem for sorting a linked lists
        assert node1 != None
        node2._next = node1._next
        node1._next = node2

    def sort(self):
        """
        This function sorts the linked list in descending 
        order by count.

        Parameters: self: object itself
    
        Returns: None

        """
        sorted = LinkedList()
        if self.head() != None:
            sorted._head = self.rm_from_hd()
        while not self.is_empty():
            # remove the next node from the original list
            sort_this = self.rm_from_hd()
            current = sorted.head()
            if current.count() < sort_this.count():
                # set the removed node as the new head.
                sorted._head = sort_this
                sort_this.set_next(current)
            else:
                while current:
                    if current.next() == None or \
                          current.next().count() < sort_this.count():
                        # insert the removed node after the current node
                        self.insert_after(current, sort_this)
                        break
                    current = current.next()
        self._head = sorted.head()

    def get_nth_highest_count(self, n):
        """
        This function returns the count associated with
        the node in the linked list at position n.

        Parameters: self: object itself
                    n: the integer position
    
        Returns: count of the node at n

        """
        n = int(n)
        position = 0
        current = self.head()
        while current is not None:
            if position == n:
                return current.count()
            position += 1
            current = current.next()
        return None
    
    def print_upto_count(self, n):
        """
        This function  print out all the words
        that have count at least n.

        Parameters: self: object itself
                    n: the integer position
    
        Returns: None

        """
        current = self._head
        while current != None:
            if current._count >= n:
                print("{} : {:d}".format(current._word, current._count))
            current = current._next
            
    def __str__(self):
        result = "Head -> "
        current = self.head()
        while current is not None:
            result += str(current) + " -> "
            current = current.next()
        result += "None"
        return result
        
def clean_title(title):
    """
    This function processes the title and cleans 
    it with the help of the string library.

    Parameters: title: the string of the title
    
    Returns: a cleaned list of the words in the title

    """
    
    cleaned_title = ""
    for char in title:
        if char not in string.punctuation:
            # remove punctuation from the title
            cleaned_title += char
        else:
            # replace punctuation with a space
            cleaned_title += ' '  
    words = cleaned_title.split()
    cleaned_list = []
    for word in words:
        if len(word) > 2:
            cleaned_list.append(word.lower())
    return cleaned_list

def main():
    input_file = input()
    n = int(input())
    words_list = LinkedList()

    file = open(input_file, 'r')
    reader = csv.reader(file)
    for row in reader:
        # check if row exists and has atleast 5 elements
        if row and len(row) > 4:
            title = row[4]
            # update word counts in the Linkedlist
            cleaned_title = clean_title(title)
            for word in cleaned_title:
                words_list.update_count(word)
    file.close()

    words_list.sort()
    k = words_list.get_nth_highest_count(n)
    if k is not None:
        words_list.print_upto_count(k)
main()