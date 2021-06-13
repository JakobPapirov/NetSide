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
from exploration.explore import explore
from helper.charChecker import charChecker
from helper.wrongInput import wrongInput

def NetSide(char):

    # Should be conditional upon whether a player is new or not
    print("You have spawned")

    alive = True

    gameState = True

    while gameState:

        # Play the game
        print("")
        print("==== Game options ====")
        print("1. Explore your surroundings.")
        print("2. Check your stats.")
        print("999. Exit the game.")
        print("==== Game options ====")
        print("")

        choiceUsr = input("What do you want to do [input number] and press enter: ")
        if choiceUsr == "":
            choiceUsr = 42
        else:
            choiceUsr = int(choiceUsr)

        if choiceUsr == 1:
            print("Exploring...")
            char, alive, foodsDiscovered = explore(char)



            if not alive:  # if alive == False
                gameState = False # exits the game
            # Commented out to save dev-time
            #print("Press 'Enter' to return to the game menu.")

        elif choiceUsr == 2:
            print("")
            print("Retrieving stats...")
            charChecker(char)
            # Commented out to save dev-time
            #print("Press 'Enter' to return to the game menu.")

        elif choiceUsr == 999:
            print("")
            print("You've chosen to exit the game.")
            print("Press 'Enter' to return to the main menu.")
            gameState = False

        else:
            wrongInput()

    return char, alive
