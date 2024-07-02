"""
    File: rhymes.py
    Author: Zayyan Essani
    Course: CSC 120, Spring 2024
    Purpose: This program analyzes a pronounciation file containing data on
             words and their pronounciations. It prompts the user for a
             word and returns all words that our perfect rhymes of that
             word. 
"""


def read_file():
    """
    Read the file of words and their pronounciations and convert into
    a dictionary with the words as keys and pronounciations as a
    list of list incase a word has two or more pronounciations.
  
    Parameters: None
  
    Returns: A dictionary that is a representation of the text file

    """
    file_name = input()
    pfile = open(file_name,"r")
    words_dict = {}
    for line in pfile:
        line_list = line.strip().split()
        
        key = line_list[0]
        # adds the words and pronounciations to a dictionary
        if key in words_dict:
            words_dict[key].append(line_list[1:])
        else:
            words_dict[key] = [line_list[1:]]
    pfile.close()
    return words_dict



def is_rhyme(words_dict):
    """
    Takes input from the user and compares it with the dictionary of words
    to find perfect rhymes of that word.
  
    Parameters: A dictionary with words as the key and prounciations
                as values of those words.
  
    Returns: None (prints the words that are perfect rhymes of the input word)

    """
    word = input().upper()
    rhymes = []
    phoneme_list = words_dict[word]
    
    for pronoun in phoneme_list:
        
        for i in range(len(pronoun)):
            if pronoun[i][-1] == '1':
                # store the primary stress and the part after it
                primary = pronoun[i:]
                pre_stress = pronoun[i-1]
                    
        for item, pronounciations in words_dict.items():
            if item != word:
                # iterate through all the pronounciations of the word
                for inner_list in pronounciations:
                    for i in range(len(inner_list)):
                        if inner_list[i][-1] == '1':
                            # compare the primary stress and the part after it
                            if inner_list[i:] == primary:
                                if inner_list[i-1] != pre_stress:
                                    rhymes.append(item)
    for items in sorted(rhymes):
        print(items)
    


def main():
    words_dict = read_file()
    is_rhyme(words_dict)
main()




