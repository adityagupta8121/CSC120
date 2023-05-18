'''
CSC 120 (A10)
File: battleship.py
Author: Aditya Gupta
Purpose: a program to read 2 given textfiles,
        which respectively reads positions of ship
        by player 1 and guesses of player 2,
        and responds to all positions in game
'''
import sys

class GridPos:
    '''
    GridPos
    An instance of this class represents given 
    grid in a 2 dimensional list
    '''
    def __init__(self, x, y, ship):
        '''
        __init__ initializes the grid at each
        position

        Parameters:
            self - instance of the same class
            x - positions, integer value
            y - positions, integer value
            ship - ship is a string

        Returns: None
        '''
        self._x = x
        self._y = y
        self._ship = ship
        self._guess = 0
    
    def __str__(self):
        '''
        __str__ string of the class

        Parameters:
            self - instance of the same class

        Returns:
            String
        '''
        if self._ship == None:
            return "N"
        else:
            return self._ship.kind

class Board:
    '''
    Board
    An instance of this class represents
    the board/grid with ship placements
    '''
    def __init__(self, list_ships, grid):
        '''
        __init__ initisalises the board
        with list of ships and grid instance

        Parameters:
            self - object instance itself
            list_ships - list of ships instances
            grid - list of gridpos instances

        Returns: None
        '''
        self._list_ships = list_ships
        self._grid = grid
    
    def guess(self, x, y):
        '''
        guess
        guess fucntion is essential for actual
        for processing the guesses.
        Checks is position is vacant to process
        the guess, or else effects the health
        of ship or it's made to sink
        
        Parameters:
            self - object instance itself
            x - int position from file
            y - int position from file

        Returns: None
        '''
        if (x < 0 or y < 0 or x > 9 or y > 9):
            print("illegal guess")
        else:
            gridpos = self._grid[x][y]
            if gridpos._ship == None:
                if gridpos._guess != 0:
                    print("miss (again)")
                else:
                    print("miss")
                gridpos._guess = 1
            else:
                if gridpos._guess != 0:
                    print("hit (again)")
                else:
                    gridpos._ship._health -= 1
                    if gridpos._ship._health == 0:
                        print("{} sunk".format(gridpos._ship))
                    else:
                        print("hit")
                gridpos._guess = 1

class Ship:
    '''
    Ship
    An instance of this class represents
    the ship in the board
    '''
    def __init__(self, list, misc):
        '''
        __init__ initisalises the ship object


        Parameters:
            self - object instance itself
            list - list of ships from read files
            misc - misc lines from file

        Returns: None
        '''
        self._misc = misc
        self._gridpos = []
        self._kind = list[0]
        self._initial_x = int(list[1])
        self._initial_y = int(list[2])
        self._final_x = int(list[3])
        self._final_y = int(list[4])
        self.occupy_gridpos()
        self.move_valid()
    
    def __str__(self):
        '''
        __str__ string of the class

        Parameters:
            self - instance of the same class

        Returns:
            String
        '''
        return self._kind
    
    def occupy_gridpos(self):
        '''
        occupy_gridpos
        occupy_gridpos checks if the position is
        occupied to find the size of ship, if it has been
        effected

        Parameters:
            self - instance of the same class

        Returns: None
        '''
        if (self._initial_x != self._final_x) \
            and (self._final_y != self._initial_y):
            print("ERROR: ship not horizontal or vertical: " + self._misc)
            sys.exit(0)

        if self._initial_x == self._final_x:
            self._size = abs(self._initial_y - self._final_y) + 1
            self._health = abs(self._initial_y - self._final_y) + 1

            for i in range(self._size):
                if self._initial_y < self._final_y:
                    self._gridpos.append((self._initial_x,self._initial_y + i))
                else:
                    self._gridpos.append((self._initial_x, self._final_y + i))

        else:
            self._size = abs(self._initial_x - self._final_x) + 1
            self._health = abs(self._initial_x - self._final_x) + 1
            
            for i in range(self._size):
                if self._initial_x < self._final_x:
                    self._gridpos.append((self._initial_x + i,self._initial_y))
                else:
                    self._gridpos.append((self._final_x + i, self._initial_y))
    
    def move_valid(self):
        '''
        move_valid
        checks if move is valid by checking the kind of ship with
        given size
        '''
        if (self._kind == 'A' and self._size != 5) \
            or (self._kind == 'B' and self._size != 4) \
            or (self._kind == 'S' and self._size != 3) \
            or (self._kind == 'D' and self._size != 3) \
            or (self._kind == 'P' and self._size != 2):
            print( "ERROR: incorrect ship size: " + self._misc)
            sys.exit(0)

def filereader(placement, guess):
    '''
    filereader
    checks for input which is processed as a ship object later
    depending on the input, being invalid, program exits
    The function proceeds to create a grid for the program
    to later check positions and ships
    Function finished the implementation of game
    by producing a board object by processing guess file

    Parameters:
        placement - data of placement file
        guess - data of guess file

    Returns: None
    '''
    list_ships = []
    grid = []

    for data in placement:
        misc = data
        data = data.split()
        ship = Ship(data, misc)
        for number in data[1:5]:
            if int(number) < 0 or int(number) > 9:
                print("ERROR: ship out-of-bounds: " + misc)
                sys.exit(0)
        if ship not in list_ships:
            list_ships.append(ship)
        elif ship in list_ships:
            print("ERROR: fleet composition incorrect")
            sys.exit(0)

    if len(list_ships) != 5:
        print("ERROR: fleet composition incorrect")
        sys.exit(0)

    for i in range(10):
        col = []
        for j in range(10):
            data_pos = None
            for ship in list_ships:
                if (i,j) in ship._gridpos:
                    if data_pos != None:
                        print("ERROR: overlapping ship: " + ship._misc)
                        sys.exit(0)
                    data_pos = GridPos(i,j,ship)
            if data_pos == None:
                data_pos = GridPos(i,j,None)
            col.append(data_pos)
        grid.append(col)

    board = Board(list_ships, grid)
    for data in guess:
        data = data.split()
        board.guess(int(data[0]),int(data[1]))
        ships_alive = 0
        for ship in board._list_ships:
            if ship._health != 0:
                ships_alive += 1
        if ships_alive == 0:
            print("all ships sunk: game over")
            sys.exit(0)

def main():
    placement = open(input()).readlines()
    guesses = open(input()).readlines()
    filereader(placement, guesses)

main()