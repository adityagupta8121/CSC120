'''
CSC 120 (A6)
File: fake_news.py
Author: Aditya Gupta
Purpose: a program to read given file,
        check titles, and check for
        unique titles/topics.
'''
import csv
import string

class Node:
    '''
    An object of the Node class represents information about a word
    given from a title. Each node/word is initialised at 1 count.
    '''
    def __init__(self, word):
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
    '''
    An object of the LinkedList class represents information about title,
    and implements nodes, which, in this case are just words.
    '''
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head == None

    def head(self):
        return self._head

    def update_count(self, word):
        '''
        update_count
        Checks for word, if word exists,
        updates the count by calling function
        incr of the Node.

        Parameters:
            self - object itself
            word - word to be checked

        Returns: None
        '''
        if self.find(word) == True:
            current = self._head
            while current != None:
                if current._word == word:
                    current.incr()
                current = current._next         
        else:
            word = Node(word)
            self.add(word)

    def find(self, given):
        '''
        find - helper function
        goes through the linkedlist to
        find/search if same word/node
        exists

        Parameters:
            self - object itself
            given - word to be checked

        Returns: 
            boolean, True if found, else False
        '''
        current = self._head
        while current != None:
            if current._word == given:
                return True
            current = current._next
        return False

    def rm_from_hd(self):
        '''
        rm_from_hd
        function taken from Shorts of PA6
        available on cloud coder

        Parameters:
            self - object itself

        Returns:
            Node - removed node
        '''
        assert self._head != None
        _node = self._head
        self._head = _node._next
        _node._next = None
        return _node

    def insert_after(self, node1, node2):
        '''
        insert_after
        function taken from Shorts of PA6
        available on cloud coder

        Parameters:
            self - object itself
            node1 - node before
            node2 - node after

        Returns: None
        '''
        assert node1 != None
        node2._next = node1._next
        node1._next = node2

    def sort(self):
        '''
        sort 
        sorts the linked list in descending
        order by _count. Function works by creating
        new LinkedList, and removing from head of
        original list.

        Parameters:
            self - object itself

        Returns: 
            Sorted LinkedList
        '''
        sorted = LinkedList()
        if self.head() != None:
            sorted.add(self.rm_from_hd())
        while not self.is_empty():
            sort_this = self.rm_from_hd()
            current = sorted.head()
            if current.count() < sort_this.count():
                sorted.add(sort_this)
            else:
                while current != None:
                    if current.next() == None or current.next().count()\
                        < sort_this.count():
                        sorted.insert_after(current, sort_this)
                        break
                    current = current.next()
        self._head = sorted.head()
        return self
    
    def add(self, node):
        '''
        add
        function taken from Shorts of PA6
        available on cloud coder

        Parameters:
            self - object itself
            node - node

        Returns: None
        '''
        node._next = self._head
        self._head = node

        
    def get_nth_highest_count(self, n):
        '''
        get_nth_highest_count
        returns the count associated with the node
        in the linked list at position n

        Parameters:
            self - object itself
            n - count

        Returns: None
        '''
        n = int(n)
        position = 0
        initial = self.head()
        current = initial
        while current != None:
            if position == n:
                return current

            position += 1
            prev = current
            next = prev.next()
            current = next

    def print_upto_count(self, n):
        '''
        print_upto_count
        print out all the words that have count at least n

        Parameters:
            self - object itself
            n - count

        Returns: None
        '''
        current = self._head
        while current != None:
            if current._count >= n:
                print("{} : {:d}".format(current._word, current._count))
            current = current._next
            
    def __str__(self):
        str = "Head ->"
        current = self.head()
        while current != None:
            str += str(current) + " ->"
            current = current.next()
        str += "None"
        return str

def read_file(filename, linked_list):
    '''
    read_file
    function to read the file, and store all data
    in the list after performing the required
    splitting/slicing operations.

    Parameters:
        filename - String, file to be read
        linked_list - linkedList object, to be worked on

    Returns: 
        data - list
    '''
    file = open(filename, 'r')
    csvreader = csv.reader(file)
    data = []

    for line in csvreader:
        if line[0][0] == '#':
            continue
        words = line[4].lower().split()

        for i in words:
            word = ''
            for letter in i:
                if letter in string.punctuation or letter in string.whitespace:
                    if len(word) <= 2:
                        word = ''
                    if len(word) > 2:
                        data.append(word)
                        word = ''
                else:
                    word += letter
            
            if len(word) > 2:    
                data.append(word)

    for count in data:
        linked_list.update_count(count)
            
    file.close()
    return data

def main():
    filename = input()
    n = input()
    linked_list = LinkedList()

    read_file(filename, linked_list)
    linked_list.sort()

    value = linked_list.get_nth_highest_count(n)
    linked_list.print_upto_count(value.count())
      
main()