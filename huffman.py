
"""
    File: huffman.py
    Author: Zayyan Essani
    Course: CSC 120, Spring 2024
    Purpose: This program priompts the user for an
             input file and builds a binary tree using
             inorder and preorder traversals. It also
             decodes an encoded sequence using the binary
             tree.
"""


class Tree:
    """This class represents a binary tree.

       The class defines the methods for defining the tree object
       and the methods for the getters and to return/print 
       the tree.
    """

    def __init__(self,value):
        """
        Initializes a Tree object by setting the node, left and right.

        Parameters:
            value: The node of the tree.
        
        Returns: None
            
        """
        self._value = value
        self._left = None
        self._right = None

    def get_left(self):
        return self._left
    
    def get_right(self):
        return self._right
    
    def get_value(self):
        return self._value
    
    def __str__(self):
        return f"({self._value} {self._left} {self._right})"
    
def create_tree(preorder, inorder):
    '''
    Creates a tree by preorder and inorder traversals

    Parameters: preorder: list of preorder traversal
                inorder: list of inorder traversal

    Returns: object representing the binary tree.
    '''

    if preorder == [] and inorder == []:
        return None
    else:
        root = preorder[0]
        
        tree = Tree(root)
        # use node index to find left and right subtree
        index = inorder.index(root)
        in_left = inorder[:index]
        in_right = inorder[index+1:]
        pre_left = preorder[1:len(in_left)+1]
        pre_right = preorder[1+len(pre_left):]
        # create tree using inorder and preorder
        tree._left = create_tree(pre_left, in_left)
        tree._right = create_tree(pre_right, in_right)
        return tree

def decode(tree, sequence):
    """
    Decodes an encoded sequence using the given tree.

    Parameters:
        tree: The binary tree used for decoding.
        sequence: The encoded sequence to be decoded.

    Returns: Decoded string

    """

    if len(sequence) == 0:
        return ""
    else:
        string = ""
        node = tree
        index = 0
        # if its 0 go left, else go right
        while index < len(sequence):
            if sequence[index] == "0":
                node = node._left
            else:
                node = node._right
            if node is None:
                return ""
            if index + 1 < len(sequence):
                # check if next bit will lead to leaf node
                if (sequence[index + 1] == "0" and node._left is None) or \
                    (sequence[index + 1] == "1" and node._right is None):
                    string += str(node._value)
                    node = tree
            # check if current node is a leaf
            if node._left is None and node._right is None:
                string += str(node._value)
                node = tree
            index += 1
        return string
    
def postorder(tree):
    """
    Performs a postorder traversal of the tree

    Parameters:
        tree: The binary tree

    Returns:
        Postorder traversal of the tree as a string
    """
 
    if tree is None:
        return ""
    else:
        return postorder(tree._left) + postorder(tree._right)\
              + str(tree._value) + " "

def make_int(slist):
    """
    This function converts the string lists to
    integer lists.
    
    Parameters: slist: string list
    
    Returns: list of integers
    """
    int_list = []
    for num in slist:
        int_list.append(int(num))
    return int_list

def main():
    filename = input('Input file: ')
    myFile = open(filename, "r")
    line_list = myFile.readlines()

    myFile.close()
    
    # find each using slicing
    preorder = make_int(line_list[0].split())
    inorder = make_int(line_list[1].split())
    sequence = line_list[2].strip()

    tree = create_tree(preorder, inorder)
    post_order_result = postorder(tree).strip()
    decode_result = decode(tree, sequence)

    print(post_order_result)
    print(decode_result)

main()
