'''
CSC 120 (A9)
File: huffman.py
Author: Aditya Gupta
Purpose: a program to read given textfile,
        run huffman codes algorithm to decode
        using preorder traversal and provide
        postoder traversal and decoded sequence.
'''
class Tree:
    '''
    Tree class
    responsible for initalising a tree
    with value as initialised value, and given 
    left/right values which can be set later.
    '''
    def __init__(self, value):
        '''
        __init__
        initialises the tree class with value,
        and NONE left, right values.

        Parameters: 
            self - object itself
            value - value of node
        '''
        self._value  = value
        self._left = None
        self._right = None

    def left(self):
        '''
        left
        returns left of the node

        Parameters:
            self - object itself

        Returns:
            left node
        '''
        return self._left
    
    def right(self):
        '''
        right
        returns right of the node

        Parameters:
            self - object itself

        Returns:
            right node
        '''
        return self._right
    
    def value(self):
        '''
        value
        returns value of the node

        Parameters:
            self - object itself

        Returns:
            value - current node
        '''
        return self._value
    
    def set_left(self, value):
        '''
        set_left
        sets value to left node

        Parameters:
            self - object itself
            value - desired value

        Returns: None
        '''
        self._left = value

    def set_right(self, value):
        '''
        set_right
        sets value to right node

        Parameters:
            self - object itself
            value - desired value

        Returns: None
        '''
        self._right = value

def decode_tree(initial, tree, string):
    '''
    decode_tree
    implemented to take input tree to decode into string
    checks for the length of string, and performs
    action accordinly to creat binary string
    It is a recursive fucntion

    Parameters:
        initial - initial tree to be on first called, used by
            function
        tree - tree that need sto be decoded
        string - binary string

    Returns:
        String string
    '''
    if len(string) == 0:
        if tree.left() == None and tree.right() == None:
            return str(tree.value())
        else:
            return ''
    elif string[0] == '0':
        if tree.left() == None and tree.right() == None:
            return str(tree.value()) + decode_tree(initial, initial, string)
        elif tree.left() != None:
            return decode_tree(initial, tree.left(), string[1:])
        else:
            return decode_tree(initial, initial, string[1:])
    else:
        if tree.right() == None and tree.left() == None:
            return str(tree.value()) + decode_tree(initial, initial, string)
        elif tree.right() != None:
            return decode_tree(initial, tree.right(), string[1:])
        else:
            return decode_tree(initial, initial, string[1:])

def process_tree(tree, preO, inO):
    '''
    process_tree
    processing preO and inO to a tree whilst
    checking conditions

    Parameters:
        tree - tree that needs to be created
        preO - preorder traversal list
        inO - inorder traversal list

    Returns:
        tree
    '''
    if len(preO) == 0 or len(inO) == 0:
        return None
    else:
        tree = Tree(preO[0])
        left_inO = inO[0:inO.index(preO[0])]
        right_inO = inO[inO.index(preO[0]) + 1:]

        preO = preO[1:]
        left_preO = preO[0:len(left_inO)]
        right_preO = preO[len(left_inO):]

        tree.set_left(process_tree(tree.left(), left_preO, left_inO))
        tree.set_right(\
            process_tree(tree.right(), right_preO, right_inO))
        return tree

def postorder_trav(tree):
    '''
    postorder_trav
    function to print postorder_traversal of the given tree
    using recursion

    Parameters:
        tree - passed tree object

    returns: 
        String
    '''
    if tree == None:
        return ''
    return postorder_trav(tree.left()) + postorder_trav(tree.right()) + \
            str(tree.value()) + ' '

def main():
    file = open(input('Input file: '))
    preo = file.readline().split()
    ino = file.readline().split()
    tree = process_tree(None, preo, ino)
    data = file.readline().strip()
    print(postorder_trav(tree))
    print(decode_tree(tree, tree, data).strip())

main()