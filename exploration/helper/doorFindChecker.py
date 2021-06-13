"""
+1 Presently, this function is specific to this one door; need to generalise it
"""
from random import randrange

import sys
sys.path.insert(0, './creation')

from exploration.exploreDoor import exploreDoor
from creation.spawn import spawnRoom

def isDoorAvailable(char):
    tempInt = char["charStats"]["int"]

    if tempInt > 1:

        # For dev-purposes
        #print("Door can be found")
        doorAvailable = True
    else:
        print("Door can't be found")
        doorAvailable = False

    return doorAvailable


def doorFinder(char):

    spawn, spawnDoor = spawnRoom()

    tempInt = char["charStats"]["int"]
    tempIntRand = randrange(101)

    if tempInt < 10 and tempIntRand > 95:
        print("You've discovered a door! 0")
        char["charSelfDisc"] = ("Door",)  # Need to add an ID later. Trying out a tuple as immutable
        # For dev-purposes
        print(tempIntRand)
        char, alive = exploreDoor(char, spawn, spawnDoor)
        input("Press 'Enter' to return to the game menu.")
    elif 10 <= tempInt < 15 and tempIntRand > 75:
        print("You've discovered a door! 1")
        char["charSelfDisc"] = ("Door",)  # Need to add an ID later. Trying out a tuple as immutable
        # For dev-purposes
        print(tempIntRand)
        char, alive = exploreDoor(char, spawn, spawnDoor)
        input("Press 'Enter' to return to the game menu.")
    elif 15 <= tempInt < 20 and tempIntRand > 50:
        print("You've discovered a door! 2")
        char["charSelfDisc"] = ("Door",)  # Need to add an ID later. Trying out a tuple as immutable
        # For dev-purposes
        print(tempIntRand)
        char, alive = exploreDoor(char, spawn, spawnDoor)
        input("Press 'Enter' to return to the game menu.")
    elif 20 <= tempInt < 30 and tempIntRand > 25:
        print("You've discovered a door! 3")
        char["charSelfDisc"] = ("Door",)  # Need to add an ID later. Trying out a tuple as immutable
        # For dev-purposes
        print(tempIntRand)
        char, alive = exploreDoor(char, spawn, spawnDoor)
        input("Press 'Enter' to return to the game menu.")
    elif 30 <= tempInt < 39 and tempIntRand > 5:
        print("You've discovered a door! 4")
        char["charSelfDisc"] = ("Door",)  # Need to add an ID later. Trying out a tuple as immutable
        # For dev-purposes
        print(tempIntRand)
        char, alive = exploreDoor(char, spawn, spawnDoor)
        input("Press 'Enter' to return to the game menu.")
    else:
        print("You've discovered a door! 5")
        char["charSelfDisc"] = ("Door",)  # Need to add an ID later. Trying out a tuple as immutable
        # For dev-purposes
        print(tempIntRand)
        char, alive = exploreDoor(char, spawn, spawnDoor)
        input("Press 'Enter' to return to the game menu.")

    return char, alive
