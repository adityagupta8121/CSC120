'''
CSC 120 (A12)
File: writer_bot_ht.py
Author: Aditya Gupta
Purpose: a program to read given textfile,
        get input from user of prefix and length
        generates new words in a random order using
        Markov chain analysis, which, is implemented
        in this program. In this program, we build
        ADT of hashtable and use instead of Python
        in-built dictionary.
'''
import sys
import random

'''
declaring global variables, as mentioned in the spec
'''
SEED = 8
NONWORD = "@"

class Hashtable:
    '''
    Hashtable class initialises an instance of Hashtable
    Object of this class is a hash table that uses linear probing
    to handle collision

    It contains, pairs (python list) and sizes
    and is responsible to access various methods like put, get
    and contains
    '''
    def __init__(self, size):
        '''
        initialises an instance of hashtable class
        using python list and size. list of pairs
        depends on size

        Parameters:
            self - object itself
            size - int

        Returns: None
        '''
        self._size = size
        self._pairs = [None] * size

    def put(self, key, val):
        '''
        hashes key and inserts the key/val pair in the hash table.
        Collisions are resolved using linear probing with decrement of -1

        Parameters:
            self - object itself
            key - key
            val - value

        Returns: None
        '''
        index = self._hash(key)
        if self.pairs()[index] is None:
            self.pairs()[index] = [key, val]
        else:
            index -= 1
            while self.pairs()[index] is not None:
                index = (index - 1) % len(self.pairs())
            self.pairs()[index] = [key, val]

    def get(self, key):
        '''
        looks up the key in the hashtable and returns corresponding
        value.

        Parameters:
            self - object itself
            key - key

        Returns:
            value related to the key
        '''
        index = self._hash(key)
        if self.pairs()[index] is None:
            return None
        elif self.pairs()[index][0] == key:
            return self.pairs()[index][1]
        index = (index - 1) % len(self.pairs())
        while self.pairs()[index] is not None and index != self._hash(key):
            if self.pairs()[index][0] == key:
                return self.pairs()[index][1]
            index = (index - 1) % len(self.pairs())
        return None

    def __contains__(self, key):
        '''
        looks up key in the hash table and checks
        if it exists

        Parameters:
            self - object itself
            key - key

        Returns:
            boolean
        '''
        if self.get(key) == None:
            return False
        return True    
    
    def _hash(self, key):
        '''
        hashes a key using horner's rule

        Parameters:
            self - object itself
            key - key

        Returns:
            hash - result
        '''
        p = 0
        for c in key:
            p = 31*p + ord(c)
        return p % self._size
    
    def size(self):
        return self._size

    def pairs(self):
        return self._pairs

    def __str__(self):
        return str(self.pairs())

def list_sentences(hash_list, hash_dict, num_of_words):
    '''
    list_sentences takes list, hashtable dictionary and
    number of words, and further creates a list of words
    that need to be converted into a sentence further.
    It works by adding 10 strings to within a lit

    Parameters:
        hash_list - list of keys, strings
        hash_dict - instance of hashtable
        num_of_words - no. of words to be generated

    Returns:
        String from resulting list_of_words
    '''
    i = 0
    list_of_words = []
    sentence_data = ""
    str = ""
    
    while len(list_of_words) != num_of_words:
        key = " ".join(hash_list)
        val = hash_dict.get(key)
        if len(val) > 1:
            list_of_words.append(val[random.randint(0, len(val) - 1)])
        elif len(val) == 1:
            list_of_words.append(val[0])
    
        hash_list.append(list_of_words[i])
        hash_list = hash_list[1:]
        i += 1
    
    while len(list_of_words) > 10:
        str = " ".join(list_of_words[0:10])
        sentence_data += str + "\n"
        str = ""
        list_of_words = list_of_words[10:]
    
    sentence_data += " ".join(list_of_words)
    return sentence_data

def insert_hash(words, hash_dict, hash_list):
    '''
    insert_hash is respobsible for taking dictionary,
    list and a list of words and places everything
    in hash_list matching key/val pairs

    Parameters:
        words - list of words to be put
        hash_dict - object of class hashtable
        hash_list - list used to insert strings to table

    Returns: None
    '''
    for ele in range(len(words)):
        key = " ".join(hash_list)
        if key in hash_dict:
            hash_dict.get(key).append(words[ele])
        else:
            hash_dict.put(key, [words[ele]])
        hash_list.append(words[ele])
        hash_list = hash_list[1:]

def main():
    random.seed(SEED)

    sfile = open(input(), "r")
    M = int(input())
    n = int(input())
    num_of_words = int(input())

    if n < 1:
        print("ERROR: specified prefix size is less than one")
        sys.exit(0)
    if num_of_words < 1:
        print("ERROR: specified size of the generated text is less than one")
        sys.exit(0)

    words = []
    for line in sfile:
        line = line.split()
        words += line

    hash_dict = Hashtable(M)
    hash_list = [NONWORD] * n
    insert_hash(words, hash_dict, hash_list)

    hash_list = [NONWORD] * n
    generated_list = list_sentences(hash_list, hash_dict, num_of_words)

    print(generated_list)

main()