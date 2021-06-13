"""
    Automate the generation of multiple food-types
        eg random => def appleGen() | def pearGen() etc
    +1 why last showInfo is always None ??
    +1 Need to add an ID to the food
"""
from objects import Apple

def foods():
    apple = Apple()
    print("Congratulations, you've found an apple and it looks like an {} variety!".format(apple.inGameName))
    print(apple.showInfo(apple.statVal))

    return apple
