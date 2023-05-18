'''
CSC 120 (A7)
File: friends.py
Author: Aditya Gupta
Purpose: This file implements
    classes from file linked_list.py
    It helps read file, create linkedList
    store friends and print them on 
    basis of common friends.
'''
from linked_list import *

def add_friend(lines):
    """
    add_friend
    adds friends individually to the LinkedList

    Parameters:
        lines - list of lines from file

    Returns:
        sorted friends linkedList
    """
    friends_list = LinkedList()

    for line in lines:
        line = line.split(" ")
        names = []
        for element in line:
            if element != "":
                names.append(element)
            sorted(names)

        if names != []:
            friend1 = Node(names[0])
            friend2 = Node(names[1])

            friends_list.add(friend1)
            friends_list.add(friend2)

            friends_list.add_friend(friend1, friend2)
            friends_list.add_friend(friend2, friend1)

    friends_list.sort()
    return friends_list

def common_friends(friends_list):
    """
    common_friends
    checks for common friends in friendList
    based on input

    Parameters:
        friends_list - Linked list of friends

    Returns: None
    """

    name1 = input("Name 1: ")
    name2 = input("Name 2: ")
    flag = True

    if not friends_list.check(name1):
        flag = False
        print ("ERROR: Unknown person "  + name1)

    if not friends_list.check(name2):
        print ("ERROR: Unknown person "  + name2)
        flag = False

    if flag:
        friendList = friends_list.common_friends(name1, name2)
        
        if len(friendList) == 0:
            print('')
        else:
            print("Friends in common:")
            for elem in friendList:
                print(elem)

def main():
    filename = input("Input file: ")
    filename = open(filename)
    content = filename.read().split("\n")
    friends_list = add_friend(content)
    common_friends(friends_list)

main()