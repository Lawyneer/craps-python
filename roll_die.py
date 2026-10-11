'''
roll_die.py - function to roll n number of dice and return the sum.

Inputs:
    num_die - number of dice to be rolled

Outputs:
    total - sum of n dice rolled

'''
# Import needed packages
import random # needed for the RNG


# Define function
def roll_die (num_die):
    
    # Initialize variables
    die = [] # list to hold value for each die rolled

    # for loop to roll each die
    for i in range(num_die):
        die.append(random.randint(1,6)) # roll ith die


    # sum the dice and return the value
    total = sum(die)
    return total
