'''
CSC 120 (A3)
File: rhymes.py
Author: Aditya Gupta
Purpose: a program to read given files, store as dictionary
        take word as input, and return words that stress 
        on same tones, i.e., return rhyming words.        
'''

def findRhyme(wordDict, word):
    '''
    findRhyme checks for rhyming words as word in the 
    dictionary which is wordDict and prints them all
    in a list, alphabetically

    Parameters: 
        wordDict - dictionary with list of words and phoneme
        word - word that needs to be compared from wordDict

    Returns: None
    '''
    finalList = []
    stress = wordDict[word]
    for stressing in stress:
        check = ['', '']
        for i in range(len(stressing)):
            if '1' in stressing[i]:
                check[0] += stressing[i - 1]
                check[1] += stressing[i]
                for j in range(stressing.index(stressing[i])+1,len(stressing)):
                    check[1] += stressing[j]
        for key, val in wordDict.items():
            for v in val:
                checking = ['', '']
                for k in range(len(v)):
                    if '1' in v[k]:
                        checking[0] += (v[k - 1])
                        checking[1] += (v[k])
                        for f in range(v.index(v[k]) + 1, len(v)):
                            checking[1] += v[f]
                if check[0] != checking[0] and check[1] == checking[1]:
                    if word == key:
                        continue
                    finalList.append(key)
    for words in sorted(finalList):
        print(words)

def read_file(pfile):
    '''
    read_file reads the file, converts everything to
    dictionary so that data is stored/organised and
    easy to access when function is called

    Parameters:
        pfile - name of the file that has to be read

    Returns:
        word_dict - dictionary with content of file (words/phoneme)
    '''
    word_dict = {}
    file = open(pfile)
    for line in file:
        line = line.strip().split()
        if line[0] not in word_dict:
            emptyList = []
            word_dict[line[0]] = emptyList        
        emptyList.append(line)
    return word_dict

def main():
    pfile = input() 
    wordDict = read_file(pfile)
    word = input().upper()
    findRhyme(wordDict, word)

main()