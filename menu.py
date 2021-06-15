# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 23:53:22 2016
Updated on

@author: Jakob Papirov

    Add later functionality to create a new char from del char, think over the structure/flow again.
    Comment function/Class calls with the expected return type, eg dictionary
    Implement https://stackoverflow.com/questions/36018401/how-to-make-a-python-program-automatically-restart-itself
        for jumping back to starting block (newPlayerCheck = True) upon character death ?
    Implement a Wall of fame for dead characters?
    +1 BUG: can't exit from first newPlayerCheck
"""

# https://stackoverflow.com/a/14999050/16139242
import sys
sys.path.insert(0, './creation')
sys.path.insert(0, './helper')
from helper.charChecker import charChecker
from helper.wrongInput import wrongInput

from helper.gameInfo import gameInfo
from killChar import killChar
from creation.createChar import createChar
from NetSide import NetSide

# ========================================== #

menuStateMaster = True
while menuStateMaster:

    # Check if new player block
    newPlayerCheck = True

    print("Welcome to NetSide!")

    while newPlayerCheck:
        menuState = True
        while menuState:
            print("")
            print("---------- Main menu ----------")
            print("These are you options:")
            print("0. Read the instructions for the game.")
            print("1. Create a character.")
            print("999. Exit the game.")
            print("---------- Main menu ----------")
            print("")
            choiceUsr = input("What do you want to do [input number and press enter]: ")
            if choiceUsr == "":
                choiceUsr = 42
            else:
                choiceUsr = int(choiceUsr)

            if choiceUsr == 0:
                print("Game instructions")
                gameInfo()
                # input("Press 'Enter' to return to the main menu.")
            elif choiceUsr == 1:
                print("Ok, let's make a character!")
                char = createChar()  # Returns dict.
                # input("Press 'Enter' to return to the main menu.")
                newPlayerCheck = False
                menuState = False
            elif choiceUsr == 999:
                # Doesn't work properly, player gets sent to the next while block anyway
                print("You have chosen to exit the game. Hope you enjoyed playing it!")
                print("BUG: Doesn't work")
                #menuStateMaster = False
                menuState = False
                newPlayerCheck = False
            else:
                wrongInput()


    # When player has a character continue below
    menuState2 = True
    while menuState2:
        print("")
        print("---------- Main menu ----------")
        print("These are you options:")
        print("0. Read the instructions for the game.")
        print("1. Enter the game!")
        print("2. Check your stats.")
        print("9. Kill your character.")
        print("999. Exit the game.")
        print("-----------------------------")
        print("")
        choiceUsr = input("What do you want to do [input number and press enter]: ")
        if choiceUsr == "":
            choiceUsr = 42
        else:
            choiceUsr = int(choiceUsr)

        alive = True

        if choiceUsr == 0:
            print("Game instructions")
            # Status:
            gameInfo()
            # input("Press 'Enter' to return to the main menu.")
        elif choiceUsr == 1:
            print("")
            print("Loading game!")
            # Later = NetSide(char, charSelfDisc)
            #char, alive = NetSide(char)
            char = NetSide(char)
            if not alive:  # if alive == False
                print("Better luck next time!")  # ask player to create a new char? Restart game?
        elif choiceUsr == 2:
            # Perhaps only available 'later'?
            char = charChecker(char, alive)
            # Commented out to save dev-time
            # input("Press 'Enter' to return to the main menu.")
        elif choiceUsr == 9:
            # killChar(char) reqs charSelfDisc at the moment
            choiceCheckKill = input("Are you sure you want to kill your character? [Y/n] ")
            subState = True
            while subState:
                if choiceCheckKill == 'Y':
                    killChar(char)
                    # Add later functionality to create a new char from here if in function
                    subState = False
                    print("")
                    input("Press 'Enter' to return to the main menu.")
                elif choiceCheckKill == 'n':
                    print("Alright, aborting...")
                    print("")
                    input("Press 'Enter' to return to the main menu.")
                    subState = False
                else:
                    # How to avoid having to go back to start menu?
                    subState = False
                    wrongInput()
        elif choiceUsr == 999:
            print("You have chosen to exit the game. Hope you enjoyed playing it!")
            menuState2 = False
            menuStateMaster = False
        else:
            wrongInput()
