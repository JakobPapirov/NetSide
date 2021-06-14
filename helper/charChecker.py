"""
    Working, small glitch with the charSelfDisc == "", not working.
    Create pure statChecker and bodyChecker
    +1 Discover you have a backpack
"""
def charChecker(char, alive):
    if alive:
        char = charCheckDisplay(char)
    else:
        print(f"{char['charSelf']} is dead.")
    #if char == "":
    #    print("You haven't created a character yet!")
    #elif char['charSelfDisc'] == "":
    #    print("{}".format(char))
    #else:
    #    charCheckDisplay(char)

    return char

def charCheckDisplay(char):
    print("")
    print("Retrieving stats...")
    print("")
    print(f"Name: {char['charSelf']}")
    print("Character stats:")
    print(f"    * Intelligence: {char['charStats']['int']} \n"
          f"    * Strength: {char['charStats']['str']}")
    print(f"Health: {char['charStatsMeta']['health']} health points")
    print(f"Location: {char['charSelfLoc']}")
    #print(f"List of discoveries: {char['charSelfDisc']}")
    print("")

    return char
