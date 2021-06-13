# Return some results later
# A player can't explore the discovered door again. Also the results aren't stored

import sys
sys.path.insert(0, './helper')

from helper.healthChecker import healthChecker

def exploreDoor(char, spawn, spawnDoor):

    alive = True

    menuState = True
    while menuState:
        print("")
        print("----------Door exploration menu----------")
        print("1. Attempt to feel for the door handle.")
        print("2. Attempt to push the door.")
        print("3. Attempt to feel the door.")
        print("4. Attempt to kick the door open.")
        print("5. Attempt to lick the door.")
        print("999. Continue exploring the door another time.")
        print("-----------------------------")
        print("")
        choiceUsr = input("What do you want to do [input number and press enter]: ")
        if choiceUsr == "":
            choiceUsr = 42
        else:
            choiceUsr = int(choiceUsr)

        if choiceUsr == 1:
            print("You feel for the door handle...")
            print("You discover that the door has a {} ".format(spawnDoor.lockType))
        elif choiceUsr == 2:
            print("You attempt to push the door...")
            print("The door doesn't budge, but it doesn't feel all that thick either; {} cm thick perhaps?".format(spawnDoor.thickness))
        elif choiceUsr == 3:
            print("You attempt to feel the door...")
            print("The feels nice to the touch; could it be {} ?".format(spawnDoor.doorMaterial))
        elif choiceUsr == 4:
            print("You attempt to kick the door open...")

            charHealthTemp = char["charStatsMeta"]["health"]
            dmg = 25 # <- May need balancing and turning into {#math}
            charHealthNew = charHealthTemp - dmg
            char["charStatsMeta"]["health"] = charHealthNew # Updates players health
            charHealthLost = charHealthTemp - charHealthNew

            print("You hurt your right leg. \nYou lose {} health \nYou now have {} health".format(charHealthLost, charHealthNew))
            char, alive = healthChecker(char)
            if not alive: # if alive == False
                menuState = False
        elif choiceUsr == 5:
            print("You attempt to lick the door...")
            print("It tastes..woody and lead paint. What is lead paint even?")
        elif choiceUsr == 999:
            print("You choose to explore the door later.")

            menuState = False
        else:
            print("You have entered the wrong input, please try again.")
            input("Press 'Enter' to return to try again.")

    return char, alive
