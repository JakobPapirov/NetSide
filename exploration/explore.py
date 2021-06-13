# Should the spawning happen here at all?!
# charSelfDisc: Need to add an ID later. Trying out a tuple as immutable
# The nested if statement doesn't work, python interprets not as intended


""" Roadmap exploration
3. first bad stuff
+1 Player should be able to find clothes! (Should clothes give + attributes?)

"""
from random import randrange

import sys
#sys.path.insert(0, './exploration/helper')
sys.path.insert(0, './helper')
sys.path.insert(0, './creation')

from doorFindChecker import isDoorAvailable, doorFinder
from foods import foods
from intItems_miscItems import notes
from strengthItems import weightDiscs
#from helper.wrongInput import wrongInput

def explore(char):

    alive = True

    # Checks if the door can be found by the player
    doorAvailable = isDoorAvailable(char)

    #print("explore > randVal: ", randVal)

    if doorAvailable: # == True
        randVal = randrange(1, 6, 1)  # Generates 1, 2, 3, 4, 5
    else: # == False
        randVal = randrange(2, 6, 1)  # Generates 2, 3, 4, 5

    # Exploring equal random chance, id doorAvailable == True, from checker
    if randVal == 1: # Chance for door
        pass
        char, alive = doorFinder(char)
    elif randVal == 2: # Chance for Food (HP)
        foodsDiscovered = []  # Empty list of discovered foods
        apple = foods() # apple should open up the options of consumption
        foodsDiscovered.append({ "apple": apple })
        #print(foodsDiscovered[0]["apple"].inGameName)
        # https://stackoverflow.com/a/53522/16139242
        if not foodsDiscovered: # = empty list
            pass
        else:
            foodChoiceUsr = input("Do you want to eat your apple? [Y/n] ") # presently, apple is specific
            if foodChoiceUsr == "":
                foodChoiceUsr = "Y"
            else:
                foodChoiceUsr = foodChoiceUsr

            if foodChoiceUsr == "Y":
                if char["charStatsMeta"]["health"] < 100:
                    print(f"You eat your {foodsDiscovered[0]['apple'].inGameName}")
                    if char["charStatsMeta"]["health"] + foodsDiscovered[0]['apple'].statVal > 100:
                        char["charStatsMeta"]["health"] = 100
                        print("Health: {} ".format(char["charStatsMeta"]["health"]))
                    else:
                        char["charStatsMeta"]["health"] = char["charStatsMeta"]["health"] + foodsDiscovered[0]['apple'].statVal
                        print(f"{char['charSelf']} has now {char['charStatsMeta']['health']} health.")
                else:
                    print("You are already at full health.")
            elif foodChoiceUsr == "n":
                print("I'll save this apple for later.")
            else:
                pass # user input failsafe?
    elif randVal == 3: # Chance for Note (Int)
        note = notes()
    elif randVal == 4: # Chance for Weight disc (Str)
        weightDiscsDiscovered = tuple()
        weightDisc = weightDiscs()

    elif randVal == 5:
        print("You didn't discover anything new.")

    return char, alive, foodsDiscovered
