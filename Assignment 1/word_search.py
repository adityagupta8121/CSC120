"""
    File: word_search.py
    Author: Aditya Gupta
    Purpose: Word search is a word game that involves searching 
            for words in a (random) grid of letters. 
            This program simulates the game by searching for words in a grid.
"""

def init():
    """
    Takes input of file names from user, stores it into global variables
  
    Parameters: None
  
    Returns: None
    """
    global wordLFile, gridFile
    wordLFile = input()
    gridFile = input()

def readFile():
    """
    Reads the word list file and the grid file, lowers the case,
    splits as required and stores them into two lists
  
    Parameters: None
  
    Returns: None
    """
    global grid, wordList, wordsFound
    grid = []
    wordList = []
    wordsFound = set()
    for elem in open(wordLFile, 'r').readlines():
        wordList.append(elem.lower().strip())
    for elem in open(gridFile, 'r').readlines():
        grid.append(elem.split())

def checkGrid():
    """
    Scans the grid row-wise, column-wise and diagonally to
    check for words by implementing occurs_in and string_parse function
  
    Parameters: None
  
    Returns: None
    """
    for ele in grid:
        parseHelper(''.join(ele))
    for elem in range(len(grid)):
        column = []
        for i in grid:
            column.append(i[elem])
        parseHelper(''.join(column))
    for eleme in range(-(len(grid) - 3), len(grid) - 2):
        line = []
        i = int(eleme < 0) * -eleme
        j = int(eleme > 0) * eleme
        k = len(grid) - abs(eleme)
        for ele in range(k):
            line.append(grid[i][j])
            i += 1
            j += 1
        occurs_in(''.join(line), wordList)

def occurs_in(string, word_list):
    """
    parses given substring into lengths of letter 3 or more
    checks the word_list
    updates wordsFound
  
    Parameters:
        string -- substring that needs to be checked
        word_list -- list of words that needs to be checked from

    Returns: None
    """
    for i in range(len(string) - 2):
        trim = string[i:]
        for j in range(len(trim), 2, -1):
            spec = trim[:j]
            if spec in word_list:
                wordsFound.add(spec)
    
def parseHelper(string):
    """
    parses given substring and reverse string to check occurs_in
  
    Parameters:
        string -- substring that needs to be checked

    Returns: None
    """
    occurs_in(string, wordList)
    occurs_in(string[::-1], wordList)

def main():
    """
    Main function that calls all functions in order.
  
    Parameters: None

    Returns: None
    """
    init()
    readFile()
    checkGrid()
    print('\n'.join(sorted(wordsFound)))

main()