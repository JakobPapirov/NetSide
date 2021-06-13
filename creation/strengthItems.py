"""
    Automate the generation of multiple food-types
        eg random => def appleGen() | def pearGen() etc
    +1 why last showInfo is always None ??
    +1 Need to add an ID to the food
"""
from objects import WeightDisc

def weightDiscs():
    weightDisc = WeightDisc()
    print("Congratulations, you've found an {}!".format(weightDisc.inGameName))
    print(weightDisc.showInfo(weightDisc.statVal))

    return weightDisc
