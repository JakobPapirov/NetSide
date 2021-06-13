# Working, small glitch with the charSelfDisc == "", not working.

def charCheckDisp(char):
    print(f"Name: {char['charSelf']}")
    print("Character stats:")
    print(f"    * Intelligence: {char['charStats']['int']} \n    * Strength: {char['charStats']['str']}")
    print(f"Health: {char['charStatsMeta']['health']} health points")
    print(f"Location: {char['charSelfLoc']}")
    print("Character body:")
    print(f"    * Heads: {char['charBody']['heads']} \n    * Ears: {char['charBody']['ears']} \n    * Eyes: {char['charBody']['eyes']} \n    * Arms: {char['charBody']['arms']} \n    * Legs: {char['charBody']['legs']} \n    * Butts: {char['charBody']['butts']} \n    * Genitaliae: {char['charBody']['genitalia']}")
    print(f"List of discoveries: {char['charSelfDisc']}")
    print("")

def charChecker(char):
    if char == "":
        print("You haven't created a character yet!")
    elif char['charSelfDisc'] == "":
        print("{}".format(char))
    else:
        charCheckDisp(char)
