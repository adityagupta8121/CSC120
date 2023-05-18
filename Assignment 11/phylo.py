'''
CSC 120 (A11)
File: phylo.py
Author: Aditya Gupta
Purpose: a program to read given textfile,
        create a binary tree, based on
        genome sequence and display
'''
from genome import *
from tree import *

def print_tree(dict_genome, tree_list):
    '''
    print_tree makes a tree from list tree_list
    taking each node and prints it accordinly

    Parameters:
        tree_list - list
        dict_genome - dictionary

    Returns: None
    '''
    while len(tree_list) > 1:
        similarity_max = 0
        t1 = None
        t2 = None
        for i in range(len(tree_list)):
            for j in range(i + 1, len(tree_list)):
                sim = tree_similarity_calc(\
                    (tree_list[i], tree_list[j]), dict_genome)
                if sim > similarity_max:
                    similarity_max = sim
                    t1 = tree_list[i]
                    t2 = tree_list[j]

        t0 = Tree(None, t1, t2, t1.leaf_genomes() | t2.leaf_genomes())
        
        if str(t1) < str(t2):
            t0.set_left(t1)
            t0.set_right(t2)
        else:
            t0.set_left(t2)
            t0.set_right(t1)

        tree_list.remove(t1)
        tree_list.remove(t2)
        tree_list.append(t0)

    print(tree_list[0])

def tree_similarity_calc(tree_pair, dict_genome):
    '''
    Takes pair of trees in a set and sictionary
    of genome; calculates similarity between each pair
    and returns maximum similar val.
    Similarity is calculated on ngram sequence basis

    Parameters:
        tree_pair = set of trees
        dict_genome - dictionary

    Returns:
        similarity_max float
    '''
    similarity_max = 0
    for organism1 in tree_pair[0].leaf_genomes():
        for organism2 in tree_pair[1].leaf_genomes():
            seq1 = set(dict_genome[organism1].ngrams())
            seq2 = set(dict_genome[organism2].ngrams())
            sim = float(len(seq1 & seq2)) / float(len(seq1 | seq2))
            if sim > similarity_max:
                similarity_max = sim
    return similarity_max

def filereader(file, N):
    '''
    function to read file data of fasta file
    set ngram, attributes and call other classes

    Parameters:
        file - filedata in list
        N - ngram size of substring

    Returns:
        list_genomes - list of genomes
        dict_genomes - dict of genomes
    '''
    list_genomes = []
    name = ''
    sequences = ''

    for line in file:
        if line[0] == (">"):
            if name != "":
                organism = GenomeData(name, sequences)
                organism.set_ngrams(N)
                list_genomes.append(organism)
            name = line.strip()
            sequences = ""
        else:
            sequences += line.strip()

    if name != "":
        organism = GenomeData(name, sequences)
        organism.set_ngrams(N)
        list_genomes.append(organism)

    dict_genome = {organism.id(): organism \
                   for organism in list_genomes}

    return list_genomes, dict_genome

def main():
    file = open(input('FASTA file: '),"r")
    N = int(input('n-gram size: '))
    data, dict_genome = filereader(file, N)

    tree_list = [Tree(organism.id(), None, None, \
                      {organism.id()}) for organism in data]
    
    print_tree(dict_genome, tree_list)

main()