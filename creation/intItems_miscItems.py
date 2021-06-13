"""
    Automate the generation of multiple food-types
        eg random => def appleGen() | def pearGen() etc
    +1 why last showInfo is always None ??
    +1 Need to add an ID to the food
"""
from random import randrange
from objects import Note

def notes():

    # Possible notes contents
        # Int-based = math question/riddles/easter eggs
        # Misc-based = some info about the game, should be very rare; much later on based on possible/available info albeit hidden
            # Smells, game-info [determine if real info or just flavour info]
    contents = "test" # WORKS!
    note = Note(contents)
    print("Congratulations, you've found an {}!".format(note.inGameName))
    #print(note.showInfo(note.statVal))
    print(note.contents)

    return note
