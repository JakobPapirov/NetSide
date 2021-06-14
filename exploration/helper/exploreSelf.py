# Connect to charChecker.py somehow - either simple ef or more

def charSelfChecker(char, *args):
    char = exploreSelf(char)
    #if char == "":
    #    print("You haven't created a character yet!")
    #elif char['charSelfDisc'] == "":
    #    print("{}".format(char))
    #else:
    #    exploreSelf(char)

    return char

def exploreSelf(char):
    print("You have:")
    print(f"    * Heads: {char['charBody']['heads']} \n"
          f"    * Ears: {char['charBody']['ears']} \n"
          f"    * Eyes: {char['charBody']['eyes']} \n"
          f"    * Arms: {char['charBody']['arms']} \n"
          f"    * Legs: {char['charBody']['legs']} \n"
          f"    * Butts: {char['charBody']['butts']} \n"
          f"    * Genitalia: {char['charBody']['genitalia']}")

    return char
