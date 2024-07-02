"""
    File: writer_bot.py
    Author: Zayyan Essani
    Course: CSC 120, Spring 2024
    Purpose: This program generates random text from a
            given source text. It uses the Markov Chain
            Algorithm.
"""


import random

SEED = 8

NONWORD = " "

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
        input_list += line
    myFile.close()
    return input_list

def create_dict(list, n):
    """
    Creates a dictionary of prefixes and suffixes from the
    given list.

    Parameters: list: list of words.
                n: length of the prefix

    Returns: dictionary with prefixes as key in the form
            of tuple and suffixes as values.
    """

    if n == 1:
        pre_dict = {(NONWORD): [list[0]]}

    elif n == 2:
        pre_dict = {(NONWORD, NONWORD): [list[0]],\
                     (NONWORD, list[0]): [list[1]]}

    elif n == 3:
        pre_dict = {
            (NONWORD, NONWORD, NONWORD): [list[0]],
            (NONWORD, NONWORD, list[0]): [list[1]],
            (NONWORD, list[0], list[1]): [list[2]]
        }

    for i in range(len(list)):
        if i + n < len(list):
            # change prefix to tuple
            prefix = tuple(list[i:i + n])
            if prefix in pre_dict:
                pre_dict[prefix].append(list[i + n])
            else:
                pre_dict[prefix] = [list[i + n]]
    
    return pre_dict

def markov_chain(words, pre_dict, n, length):
    
    """
    Generates random text using the Markov Chain
    Algorithm.
  
    Parameters: words: list of words
                pre_dict: dictionary of prefixes and suffixes.
                n: length of prefix
                length: length of generated text
  
    Returns: list of generated words

    """

    gen_words = words[:n]
    pre_tup = tuple(gen_words)
    # generate random text based on algorithm
    while pre_tup in pre_dict and len(gen_words) < length:
        suff_list = pre_dict[pre_tup]
        if len(suff_list) == 1:
            position = 0
        else:
            position = random.randint(0, len(suff_list) - 1)  
        new_word = suff_list[position]
        gen_words.append(new_word)
        # update tuple with latest words
        pre_tup = tuple(gen_words[-n:])
    return gen_words



def generate_text(gen_words):
    """
    Prints the generated text.
  
    Parameters: list of generated words
  
    Returns: None

    """

    text = []

    for i in range(len(gen_words)):
        text[-1].append(gen_words[i])

    for line in text:
        # convert to string
        line = ' '.join(line)
        print(line)

def main():
    # set seed for random number generator
    random.seed(SEED)

    filename = input()
    n = int(input())
    num_words = int(input())

    input_list = read_file(filename)
    pre_dict = create_dict(input_list, n)
    generated_text = markov_chain(input_list, pre_dict, n, num_words)
    # print with 10 words per line
    words_per_line = 10
    for i in range(0, len(generated_text), words_per_line):
        print(' '.join(generated_text[i:i + words_per_line]))


main()
