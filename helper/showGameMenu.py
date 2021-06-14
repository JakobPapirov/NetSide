

import sys
sys.path.insert(0, './helper')
sys.path.insert(0, './exploration')
sys.path.insert(0, './exploration/helper')

from helper.charChecker import charChecker
from exploration.helper.exploreSelf import charSelfChecker
from exploration.explore import explore
from helper.netSideExit import netSideExit
from helper.wrongInput import wrongInput


def gameMenuChecker(char, eventCheck, alive):
    # Function selects available game options to the player, based on eventCheck:: dictionary

    # https://www.geeksforgeeks.org/python-get-key-from-value-in-dictionary/
    keyList = list(eventCheck.keys())

    menu = [] # The list of True = available game options
    for key in keyList:
        if eventCheck[key]: # === if eventCheck[key] == True:
            menu.append(key)
        else:
            pass

    char = showGameMenu(char, menu, eventCheck, alive)
    return char


def showGameMenu(char, menu, eventCheck, alive):
    # Function generates a menu based on available options
        # Prints menu and numbers(?) them
        # Unable to set 999 = exit then

    print("")
    print("==== Game options ====")
    for key in menu:
        print(f"{(menu.index(key) + 1)}: {key}")
    print("==== Game options ====")
    print("")

    choiceUsr = input("What do you want to do [input number] and press enter: ")

    # Bug; character => error
    if choiceUsr == "":
        choiceUsr = 42
    else:
        choiceUsr = int(choiceUsr)

    char = choiceUserMenu(char, choiceUsr, menu, eventCheck, alive)
    print("showGameMenu")
    print(char)
    return char


def choiceUserMenu(char, choiceUsr, menu, eventCheck, alive):
    # Should react to player choice and fire correct function that resolves player choice

    choiceUserOptions = {
        "Explore your surroundings": explore,
        "Explore yourself": charSelfChecker,
        "Consume food": "eatFood",
        "Train strength": "StrTrain",
        "Explore Notes": "Notes",
        # Move file to exploration/helper later
        "Check your stats": charChecker,
        "Exit the game": netSideExit,
        "Wrong input": wrongInput
    }
    # choiceUsr :: int
    # menu :: list
    # Add try/catch block to simulate player entering wrong input
    playerChoiceInterpreted = menu[choiceUsr - 1] # Returns a str => used as key choiceUserOptions
    # choiceUsr can only be 1, 2, 3 on the default pass-through
    # => menu[1, 2, 3] => playerChoiceInterpreted = "Explore yourself",
    #                                                   "Check your stats",
    #                                                   "Exit the game",

    # might need to rename var
    # keyListUserOptions :: list
    keyListUserOptions = list(choiceUserOptions.keys())
    print(keyListUserOptions)

    #listNums = range(len(keyListUserOptions))
    #listNums = list( range( len(keyListUserOptions) ))

    # Add alive /Overlord\
    char = choiceUserOptions[playerChoiceInterpreted](char, alive)

    print("choiceUserMenu post")
    print("Status: ", alive)

    #return char, eventCheck, alive
    return char
