'''
CSC 120 (A5)
File: ngrams.py
Author: Aditya Gupta
Purpose: a program to read given file, and
        number which computes the maximum
        number of times an N-gram occurs.
'''
class Input:
    '''
    An object of the Input class represents 
    information about the input data.
    '''
    def __init__(self):
        self._data = open(input()).read()

    def wordlist(self):
        '''
        wordList reads the file, splits into list, removes
        punctuation and removed empty space.

        Parameters:
            self - calling the object itself

        Returns:
            self._data - list of words edited
        '''
        self._data = self._data.split()
        for word in range(len(self._data) - 1, -1, -1):
            self._data[word] = \
            self._data[word].strip('~!@#$%^&*()-=_+[];,./:<>?|}{\\\'\"')
            self._data[word] = self._data[word].lower()
            if self._data[word] == '':
                del self._data[word]
        return self._data

class Ngrams:
    '''
    An object of this class represents n-gram
    information about the input list of words.
    '''

    def __init__(self):
        self._n = int(input())
        self._dictgram = {}

    def update(self, ngram):
        self._dictgram[ngram] += 1

    def process_wordlist(self, wordlist):
        '''
        process_wordlist processes the list - wordlist,
        to compute the number of times each n-gram occurs

        Parameters:
            self - calling the object itself
            wordlist - list of the words that are to be checked

        Returns: None
        '''
        combination = []
        for i in range(0, len(wordlist) - self._n + 1):
            combination.append(tuple(wordlist[i : i + self._n]))

        i = self._n
        while not i >= len(combination):
            for j in range(len(combination) - 1, i - 1, -1):
                if combination[i] == combination[j]:
                    if combination[j] in self._dictgram:
                        self._dictgram[combination[i]] += 1
                    else:
                        self._dictgram[combination[i]] = 1
                    del combination[j]

        for j in range(0, len(combination)):
            if combination[j] in self._dictgram:
                self._dictgram[combination[j]] += 1
            else:
                self._dictgram[combination[j]] = 1

    def print_max_ngrams(self):
        '''
        print_max_ngrams prints n-grams as required in the
        given format, and is responsible to also make sure
        alphabetic pattern.

        Parameters:
            self - calling the object itself

        Returns: None
        '''
        maxi_gram = []
        maxi = 0
        for gram in self._dictgram:
            if self._dictgram[gram] > maxi:
                maxi = self._dictgram[gram]
                maxi_gram = [gram]
            elif self._dictgram[gram] == maxi:
                maxi_gram.append(gram)

        maxi_gram = sorted(maxi_gram)
        for i in range(0, len(maxi_gram)):
            gram_str = maxi_gram[i][0]
            for j in range(1, len(maxi_gram[i])):
                gram_str += (' ' + maxi_gram[i][j])
            print("{:d} -- {}".format(maxi, gram_str))
    
def main():
    get = Input()
    word_list = get.wordlist()
    gram = Ngrams()
    gram.process_wordlist(word_list)
    gram.print_max_ngrams()

main()