'''
CSC 120 (A11)
File: genome.py
Author: Aditya Gupta
Purpose: a program to initialise
    genome, create ngram and set 
    respective attributes
'''

class GenomeData:

    def __init__(self, name, sequence):
        '''
        this class initialises object of genome data
        and all the other attributes

        It is initialised with id, string sequence.
        '''
        self._id = name.split()[0][1:]
        self._sequence = sequence.strip()
        self._ngrams = set()

    def set_ngrams(self, n):
        '''
        sets ngrams to genomedata object based on n
        whiich is size of the string

        Parameters:
            n - int

        Returns: None
        '''
        self._ngrams = set([self._sequence[i : i + n] \
                            for i in range(len(self._sequence) - n + 1)])

    def id(self):
        return self._id

    def seq(self):
        return self._sequence

    def ngrams(self):
        return self._ngrams
    
    def __str__(self):
        return "id: {}, Sequence: {}, NGrams: {}"\
            .format(self._id, self._sequence, self._ngrams)