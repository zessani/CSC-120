
"""
    File: writer_bot_ht.py
    Author: Zayyan Essani
    Course: CSC 120, Spring 2024
    Purpose: This program generates random text from a given
            source text. It uses the Markov Chain Algorithm 
            and a hash table ADT.
"""

import random
import sys

SEED = 8
NONWORD = "@"


def read_file(filename):
    """
    Read the file of source text and split the line
    into a list with no empty spaces.
  
    Parameters: name of file
  
    Returns: list of words from file.

    """
    input_list = []
    myFile = open(filename, "r")
    for line in myFile:
        line = line.strip().split()
        input_list.extend(line)
    myFile.close()
    return input_list


class Hashtable:

    """This class represents a hash table.

       The class defines the methods for defining Hashtable
       object and the methods for the hashing the keys and 
       inserting. And the method for looking up the key and getters.
        
    """
    def __init__(self, size):
        """
        Initializes a Hashtable object with a given size.

        Parameters:
            size (int): The size of the hash table.
        
        Returns: None
            
        """
        self._pairs = [None] * size
        self._size = size
    
    def put(self, key, value):
        """
        Puts a key-value pair into the hash table.

        Parameters:
            key: The key to be inserted.
            value: The value associated with the key.

        Returns: None
        """
        i = self._hash(key)
        while self._pairs[i] != None:
            i -= 1
            if i < 0:
                i = len(self._pairs) - 1
        self._pairs[i] = [key, value]
    
    def get(self, key):
        """
        Gets the value associated with the key from the hash table.

        Parameters:
            key: The key to retrieve the value for.

        Returns:
            The value associated with the key, or None if not found.
        """
        i = self._hash(key)
        while self._pairs[i] != None:
            if self._pairs[i][0] == key:
                return self._pairs[i][1]
            i -= 1
            if i < 0:
                i = len(self._pairs) - 1
        return None
    
    def add(self, key, value):
        """
        Adds a value to the list associated with the given key.

        Parameters:
            key: The key to add the value to.
            value: The value to add to the list.

        Returns: None
        """
        
        i = self._hash(key)
        while self._pairs[i][0] != key:
            i -= 1
            if i < 0:
                i = len(self._pairs) - 1
        self._pairs[i][1].append(value)
    
    def _hash(self, key):
        """
        Calculates the hash value of the key.

        Parameters:
            key: The key to calculate the hash value for.

        Returns:
            The hash value of the key.
        """
        p = 0
        for c in key:
            p = 31 * p + ord(c)
        return p % self._size
    
    def __contains__(self, key):
        """
        Checks if the hash table contains the given key.

        Parameters:
            key: The key to check for.

        Returns:
            True if the key is found in the hash table, 
            False if not.
        """
        i = self._hash(key)
        while self._pairs[i] != None:
            if self._pairs[i][0] == key:
                return True
            i -= 1
            if i < 0:
                i = len(self._pairs) - 1
        return False
    
    def __str__(self):
        for i in range(self._size):
            if self._pairs[i] != None:
                pair = self._pairs[i]
                print("{} : {}/{}".format(i, pair[0], pair[1]))

def markov_chain(hash_list, hash_dict, num_of_words):
    """
    Generate text using the Markov Chain Algorithm.

    Parameters:
        hash_list (list): The list used for Markov chain.
        hash_dict (Hashtable): The hash table.
        num_of_words (int): The number of words to generate.

    Returns:
        string_data: The generated text.
    """
    i = 0
    list_of_words = []
    string_data = ""
    string = ""
    
    while len(list_of_words) != num_of_words:
        key = " ".join(hash_list)
        values = hash_dict.get(key)
        if len(values) > 1:
            # If there are multiple values, randomly choose one
            list_of_words.append(values[random.randint(0, len(values) - 1)])
        elif len(values) == 1:
            list_of_words.append(values[0])
    
        hash_list.append(list_of_words[i])
        hash_list = hash_list[1:]
        i += 1
    
    while len(list_of_words) > 10:
        string = " ".join(list_of_words[0:10])
        string_data += string + "\n"
        string = ""
        list_of_words = list_of_words[10:]
    
    string_data += " ".join(list_of_words)
    return string_data

def hash_insert(word_list, hash_dict, hash_list):
    """
    Insert words into the hash table.

    Parameters:
        word_list (list): List of words.
        hash_dict (Hashtable): The hash table.
        hash_list (list): The list used for hashing.

    Returns: None
    """
    for element in range(len(word_list)):
        key = " ".join(hash_list)
        if key in hash_dict:
            hash_dict.get(key).append(word_list[element])
        else:
            # add a new pair to the hash table
            hash_dict.put(key, [word_list[element]])
        hash_list.append(word_list[element])
        hash_list = hash_list[1:]


def main():
    random.seed(SEED)

    filename = input()
    object_size = int(input())
    prefix_size = int(input())
    num_words = int(input())
    # check if sizes are valid
    if prefix_size < 1:
        print("ERROR: specified prefix size is less than one")
        sys.exit(0)
    if num_words < 1:
        print("ERROR: specified size of the generated text is less than one")
        sys.exit(0)

    word_list = read_file(filename)

    hash_dict = Hashtable(object_size)
    # create initial prefix list
    hash_list = [NONWORD] * prefix_size
    hash_insert(word_list, hash_dict, hash_list)

    hash_list = [NONWORD] * prefix_size
    generated_list = markov_chain(hash_list, hash_dict, num_words)

    print(generated_list)

main()
