# -*- coding: utf-8 -*-
"""
Created on Mon Jun 7 18:42 2021
Updated on Mon Jun 7 19:26 2021

@author: Jakob Papirov

    Check to see if variables are non-empty
    Commands are not possible - how to give the player knowledge of new commands?
    +1 Presently, after door is discovered player can't explore it again.
    No menuState | Good | Bad?
    Expand options as the player improves (eg learns in a Note how to do push-ups -> can train Str)
"""
import sys
sys.path.insert(0, './exploration')
sys.path.insert(0, './helper')

from helper.showGameMenu import gameMenuChecker


#from helper.wrongInput import wrongInput
#from helper.netSideExit import netSideExit

def NetSide(char):

    alive = True

    eventCheck = {
        "Explore your surroundings": False,
        "Explore yourself": True,
        "Consume food": False,
        "Train strength": False,
        "Explore Notes": False,
        "Check your stats": True,
        "Exit the game": True
    }

    # no while loop right now, goes back to main-menu
    #char, eventCheck, alive = gameMenuChecker(char, eventCheck, alive)
    char = gameMenuChecker(char, eventCheck, alive)

    #return char, alive
    return char
