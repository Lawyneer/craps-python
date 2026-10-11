'''
play_craps.py - script to allow a user to play a simple text based game of craps.

Inputs:
    bet - user input bet amount
    line - user input to select a pass or don't pass line bet
    
Outputs:
    Print if the player wins, loses, pushes, and how much was won/lost.
    Other functions called from within print out rolls as shooter rolls

Notes:
    This has been run and tested on linux and Mac machines.
    
'''

# Import needed packages
import craps as crps    # function to play craps
import get_valid_input as gvi
from os import system, name 
from game_constants import PASS_LINE, DONT_PASS

# Initialize variables
bank_roll = 500     # starting bankroll
keep_playing = 1    # termination condition


while(keep_playing == 1 and bank_roll > 0):
    
    # Clear screen from last game
    if(name == 'nt'): # Windows machine
        _ = system('cls')
    else: # linux and Mac machines
        _ = system('clear')
        
    # Prompt user for a bet
    bet = gvi.get_valid_input("Please enter a bet.\n", range(1, bank_roll +1))

    # Prompt user to line    
    line = gvi.get_valid_input("Enter 1 for a pass line bet and 2 for a Don't Pass Line bet.\n", (PASS_LINE, DONT_PASS))

        
    # Play the game
    win = crps.craps(bet, line)
    
    # Print results
    if(win < 0): # print lose
        print("The shooter lost -$",abs(win),".\n")
    elif(win > 0): # Print win
        print("The shooter won $", win, "\n")
    else: # print push
        print("The shooter pushes")
    
    # Update bankroll
    bank_roll = bank_roll + win
    print("Current bankroll is: $",bank_roll,"\n")
    
    # Determine if play continues
    if(bank_roll <= 0): # Check if player busted
        print("You're bust.  Please try again.\n")
    else: # prompt user to keep playing
        keep_playing = gvi.get_valid_input("Enter 1 to keep playing or 0 to quit.\n", (0, 1))
