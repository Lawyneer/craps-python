'''
keep_rolling.py - function that returns an indication of winning or losing
                   when a point is established in a craps game

Inputs:
     point - point shooter rolled

Outputs:
    win - indicateion of winning or losing: 1 = win, -1 = lose

Notes:
    1.  Comment out the print statements in the if, elif, else for large
        simulations.  The are included here to allow the user to actually
        simulate playing craps
    
    2.  'else' statement includes a randomly selected delay from 1 to 5 seconds
        as a shooter keeps rolling.  This provides some suspense while allowing
        the user to see what happens instead of just printing a lot of information
        to the screen all at once.
'''

 # Import needed modules
import random           # needed for the RNG
import roll_die as roll # import the function to roll dice
import time             # needed to pause after rolling die for effect
from game_constants import SHOOTER_WINS, SHOOTER_LOSES


# Define function
def keep_rolling(point):
      
    while True:
        roll = roll.roll_die(2)
        # shooter won
        if roll == point:
            return SHOOTER_WINS
        # shooter lost
        if roll == 7:
            return SHOOTER_LOSES
        
        print("Shooter rolled:", roll, "\n")
        time.sleep(random.randint(1,5))
