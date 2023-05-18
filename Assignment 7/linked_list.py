'''
CSC 120 (A7)
File: linked_list.py
Author: Aditya Gupta
Purpose: This file consists of two classes,
    which are used in friends.py. The two classes are:
    LinkedList and Node. LinkedList class and Node are
    related/connected to each other.
'''
class Node:
    """
    The node class defines a node in LinkedList containing one person,
    who is the friend, and therefore, it is the linkedlist of the person
    and their friends as next/friends.

    A node is initialised with name, and having no friends.
    """
    def __init__(self, name):
        self._name = name
        self._friends = None
        self._next = None

    def name(self):
        return self._name

    def friends(self):
        return self._friends

    def next(self):
        return self._next

    def set_next(self, target):
        """
        set_next
        Sets the next node as target.

        Parameters:
            self - object itself
            target - target node to be set

        Returns: None
        """
        self._next = target

    def set_friends(self, target):
        """
        set_friends
        Sets the friends node as target.

        Parameters:
            self - object itself
            target - target node to be set

        Returns: None
        """
        self._friends = target

    def __str__(self):
        return "Name: " + self._name + ", Friends: " + str(self._friends) + ", Next: " + str(self._next) + "; "

class LinkedList:
    """
    The class LinkedList is a list of nodes, containing friends.
    Uses the Node class.
    
    A LinkedList is initialised as empty.
    """
    def __init__(self):
        self._head = None

    def head(self):
        return self._head
    
    def check(self, name):
        """
        check
        checks if the name of person is present
        in the linkedlist, returns true if yes.

        Parameters:
            self - object itself
            name - to be checked

        Returns: true or false
        """
        current = self.head()
        while current != None:
            if current.name() == name:
                return True
            current = current.next()
        return False

    def add(self, node):
        """
        add
        Adds name of person to LinkedList if name
        does not exist.

        Parameters:
            self - object itself
            node - to be added

        Returns: None
        """
        if not self.check(node.name()):
            node.set_next(self.head())
            self._head = node

    def add_friend(self, node1, node2):
        """
        add_friend
        adds the friend of person to their List
        node2 is made friends with node 1.

        Parameters:
            self - object itself
            node1 - friend
            node2 - friend to be added

        Returns: None
        """
        new_node = Node(node2.name())
        current = self.head()
        while current != None:
            if current.name() == node1.name():
                break
            current = current.next()
        new_node.set_next(current.friends())
        current.set_friends(new_node)

    def find(self, name):
        """
        find
        finds the node linked to the name

        Parameters:
            self - object itself
            name - name to be linked found

        Returns: 
            friends
        """
        current = self.head()
        while current != None:
            if current.name() == name:
                break
            current = current.next()
        return current.friends()

    def common_friends(self, name1, name2):
        """
        common_friends
        Checks the friends of name1 and name2 and returns list of
        common friends

        Parameters:
            name1 - name of friend 1
            name2 - name of friend 2

        Returns:
            List of friends
        """
        list1 = []
        self.sort()
        friend1 = self.find(name1)
        friend2 = self.find(name2)
        one_friend = False

        while friend1 != None:
            while friend2 != None:
                if friend1.name() == friend2.name():
                    if not one_friend:
                        one_friend = True

                    list1.append(friend1.name())
                
                friend2 = friend2.next()
            
            friend1 = friend1.next()
            friend2 = self.find(name2)
        
        return sorted(list1)


    def __str__(self):
        current = self.head()
        while current != None:
            str += str(current) + ">"
            current = current.next()
        return str
    
    def sort(self):
        """
        sort
        sorts the linkedList using a new LinkedList
        on the basis of friends' names
        """
        sorted = LinkedList()
        while self._head != None:
            current_elem = self.remove()
            if sorted._head == None:
                sorted._head = current_elem
            else:
                temp = sorted._head
                while temp != None:
                    if str(current_elem._friends) > str(temp._friends):
                        E = temp
                        sorted._head = current_elem
                        sorted._head._next = E
                        break
                    if str(temp._friends) >= str(current_elem._friends) and temp._next == None or \
                    str(temp._next._friends) < str(current_elem._friends):
                        sorted.insert(temp, current_elem)
                        break
                    temp = temp._next
                
        self._head = sorted._head
    

    def insert(self, node1, node2):
        """
        Taken from shorts of PA6
        """
        assert node1 != None
        node2._next = node1._next
        node1._next = node2
    
    def remove(self):
        """
        Taken from shorts of PA6
        """
        assert self._head != None
        _node = self._head
        self._head = _node._next
        _node._next = None
        return _node