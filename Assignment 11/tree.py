'''
CSC 120 (A11)
File: tree.py
Author: Aditya Gupta
Purpose: a program to initialise
    tree object, create the structure
    by setting children/attributes
'''

class Tree:
    '''
    Tree class creates a tree object,
    helps to add id/genome
    check if leaves are present
    set left/right nodes.
    '''
    def __init__(self, name, left, right, leaf_genomes):
        '''
        initialises the tree object,
        and all required attributes

        Parameters:
            self - object itself
            name - str
            left - nodes
            right - nodes
            leaf_genomes - ids on leaf nodes
        
        Returns - None
        '''
        self._name = name
        self._left = left
        self._right = right
        self._leaf_genomes = leaf_genomes
    
    def is_leaf(self):
        '''
        checks if given node is a leaf

        Parameters:
            self - object itself
        
        Return: None
        '''
        return None == self._left == self._right
    
    def name(self):
        return self._name
    
    def left(self):
        return self._left

    def right(self):
        return self._right

    def set_name(self, name):
        self._name = name
    
    def set_left(self, left):
        self._left = left
        
    def set_right(self, right):
        self._right = right
    
    def leaf_genomes(self):
        return self._leaf_genomes
    
    def set_leaf_genomes(self, leaf_genomes):
        self._leaf_genomes = leaf_genomes

    def __str__(self):
        if self.is_leaf():
            return self.name()
        else:
            return "({}, {})".format(str(self.left()), str(self.right()))
