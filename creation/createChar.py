# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 00:15:27 2016
@author: Jakob Papirov

# Add disc to the char!
"""

import sys
sys.path.insert(0, '')

from creation.charShell import Character, Human

def createChar():

    print("Creating your character!")

    # Generates a generic Character
    emptyCharShell = Character() # Needed? Find out! PyCharm says not used

    # Generates a Human Character
    emptyCharShell = Human() # Overrides the generic emptyCharShell

# Commented out to save dev-time
#    charName = input("Please name your character: ")
#    if charName == "":
#        charName = "Xena"
#    else:
#        charName = charName

    charName = "Xena"
    # Write in an fail-safe to let user confirm name of character
    print("")
    print("Character name {} is created!".format(charName))
    char = emptyCharShell.generateHuman(charName)

    charSelfDisc = tuple()
    char.update({ "charSelfDisc": charSelfDisc })

    return char
