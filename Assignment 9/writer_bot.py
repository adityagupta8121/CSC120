'''
CSC 120 (A9)
File: writer_bot.py
Author: Aditya Gupta
Purpose: a program to read given textfile,
        get input from user of prefix and length
        generates new words in a random order using
        Markov chain analysis, which, is implemented
        in this program.
'''
import random

'''
declaring global variables, as mentioned in the spec
'''
SEED = 8
NONWORD = " "
     
def create_tuple(word, n):
    '''
    create_tuple
    creates a tuple of word, n times

    Parameters:
        word - tuple to be created of word
        n - number of times to be repeted

    Returns:
        tuple tup
    '''
    tup = []
    for i in range(n):
        tup.append(word)
    return tuple(tup)

def shift_tuple(tup, value):
    '''
    shift_tuple
    taken from shorts

    Parameters:
        tup - tuple
        value - shift by value

    Returns:
        t tuple
    '''
    t = tup[1:]
    t = t + (value,)
    return t

def make_prefix(text, prefix):
    '''
    make_prefix
    wmakes prefix of the given text on the prefix
    
    Parameters:
        text - file data
        prefix - length

    Returns:
        temp list
    '''
    temp = []
    for items in text[:prefix]:
        temp.append(items)
    temp = tuple(temp)
    return temp

def filereader(file_name):
    '''
    filereader
    reads a file and strips/splits to store
    data in a list

    Parameters:
        file_name - name of file
    Returns:
        list data
    '''
    data = []
    file = open(file_name)
    for i in file:
        i = i.strip().split()
        data += i
    return data

def create_dictionary(data, prefix):
    '''
    create_dictionary
    takes data and prefix to make dictionary
    finds possible prefixes, looping through data

    parameters:
        data - data from file
        prefix - count of prefix

    returns:
        word_dict
    '''
    word_dict = {}
    key = create_tuple(NONWORD, prefix)
    for word in range(len(data)):
        if key in word_dict:
            word_dict[key].append(data[word])
        else:
            word_dict[key] = [data[word]]
        key = shift_tuple(key, data[word])
    return word_dict

def format_print(file_data, n, no_words, dic):
    '''
    format_print
    stores words in a list, in a random order
    it makes prefix based on user input, and if it
    exists in dictionary, a random prefix is selected
    to move to another tuple, and further
    prinst the output in 10 per line till it reacher
    no_words. in count

    Parameters:
        file_data - data from file
        n - prefix shift
        dic - dictionary
        no_words - number of words
    '''
    word = ''
    words = []
    counter = no_words
    for i in file_data[:n]:
        words.append(i)

    prefix = make_prefix(file_data, n)

    for text in range(no_words+1):
        if prefix in dic:
            if len(dic[prefix]) > 1:
                word = dic[prefix][random.randint(0, len(dic[prefix]) - 1)]
            else:
                word = dic[prefix][0]
        words.append(word)
        prefix = shift_tuple(prefix, word)

    for i in range(0, no_words, 10):
        if counter >= 10:
            print(' '.join(words[i: i + 10]))
        else:
            print(' '.join(words[i: i + counter]))
        counter -= 10

def main():
    random.seed(SEED)
    sfile = input()
    n = int(input())
    no_words = int(input())

    file_data = filereader(sfile)
    markov_algo = create_dictionary(file_data, n)

    format_print(file_data, n, no_words, markov_algo)

main()