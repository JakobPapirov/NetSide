# add kill char later

def healthChecker(char):
    charHealthTemp = char["charStatsMeta"]["health"]
    if charHealthTemp > 0:
        alive = True
    else:
        print(f"{char['charSelf']} dies.")
        alive = False

    return char, alive
