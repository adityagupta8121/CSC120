"""
    File: word_grid.py
    Author: Aditya Gupta
    Purpose: This program involves learning to use Python’s 
            random number generator.
"""
import random  

def init():
    """
    Takes input of of grid_size and seed_value from the user
    and initialises random value generator
  
    Parameters: None
  
    Returns: None
    """
    global grid_size     
    grid_size = int(input())
    seed_value = input()
    random.seed(seed_value)
    
def make_grid(grid_size):  
    """
    Creates and returns a grid of size grid_size × grid_size 
    whose elements are randomly generated letters
  
    Parameters:
        grid_size -- size of the grid mentioned by user
  
    Returns:
        grid -- essentially a list of grid_size no. of rows
    """   
    grid = []
    for ele in range(grid_size):         
        i = []
        for elem in range(grid_size):             
            randomAlph = random.randint(97,122)             
            i.append(chr(randomAlph))         
        grid.append(i)     
    return grid  
    
def print_grid(grid): 
    """
    Takes a grid (i.e., list of lists) as an argument and 
    prints it out one row per line, 
    with a single comma after each letter except 
    for the last one in the row .

    Parameters:
        grid -- essentially a list of grid_size no. of rows
  
    Returns: None
    """   
    
    for ele in range(len(grid)):         
        i = ','.join(grid[ele]).strip(',')         
        
        print(i)  

def main(): 
    """
    Main function that calls all functions in order.
  
    Parameters: None

    Returns: None
    """

    init() 
    grid = make_grid(grid_size) 
    print_grid(grid)     

main()