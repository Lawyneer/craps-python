'''
craps.py - function that returns the amount won or lost from a single game of craps.

Inputs:
    bet - an amount bet on either the pass or don't pass line
    line - 1 for the pass line and 2 for the don't pass line

Outputs:
    winnings - the amount of money a player won/lost.  See note 2.

Notes:
    1.  Right now the code is set for a player winning even money on a pass or don't
        pass line bet.  Working on the code to include taking/laying odds.

    2.  Comment out the print statements for large simulations.  The are included 
        here to allow the user to actually simulate playing craps.

'''
# Import needed modules
import roll_die as roll     # function to roll dice
import keep_rolling as kr   # function to keep rolling when a point is set
from game_constants import PASS_LINE, DONT_PASS, SHOOTER_WINS, SHOOTER_LOSES


# Define function
def craps( bet, line):

    # Establish point
    point = roll.roll_die(2)            # roll dice
    print("The point is: ", point,"\n") # print point

    # Determine outcome of game
    if (point == 7 or point == 11): # shooter rolls 7 or 11 on come out roll
        if (line == PASS_LINE):     # pass line win
            winnings = bet  # player wins bet
            print("Pass line shooter wins with a ",point,"\n") # print winner
        else: # don't pass line loser
            winnings = -bet # player loses bet
            print("Don't pass line shooter loses with a ",point,"\n") # print loser 
    
    elif point in (4, 5, 6, 8, 9, 10):
        outcome = kr.keep_rolling(point)
        if((outcome == SHOOTER_WINS) == (line == PASS_LINE)):
            winnings = bet
        else:
            winnings = -bet

    elif (point == 2 or point == 3): # shooter rolls 2 or 3 on come out roll
        if (line == PASS_LINE): # pass line lose
            winnings = -bet # player loses bet
            print("Pass line shooter loses with a ", point, "\n") # print lose
        else: # don't pass line win
            winnings = bet  # player wins bet
            print("Don't pass line shooter loses with a ", point, "\n") # print win

    
    else: # shooter rolled a 12 on come out roll
        if (line == PASS_LINE): # pass line lose
            winnings = -bet # player loses bet
            print("Pass line shooter loses with a ", point, "\n") # print lose
        else: # don't pass line push
            winnings = 0    # player neither wins or loses bet
            print("Don't pass line shooter pushes with a ", point, "\n") # print push

    return winnings # return winnings
