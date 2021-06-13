""""
Should I Capitalise words? What's best for the player?
"""
import random

class Object:
    def __init__(self, name, weight, color, taste, texture, cat, objType):
        #self.ID = 0 # Add later, increment
        self.inGameName = name
        self.weight = weight
        self.color = color
        #self.desc = desc # Some sort of description
        self.taste = taste
        self.texture = texture
        self.cat = cat # Rename?
        self.statType = objType # Rename?

    def showInfo(self, *args):
        print("Name: ", self.inGameName)
        print("Weight: ", self.weight, "g")
        print("Color: ", self.color)
        print("Taste: ", self.taste)
        print("Texture: ", self.texture)
        print("Category: ", self.cat)
        print("Stats type: ", self.statType)
        print("Stat value: ", args)

# Trying out specific generators / classes
class Apple(Object):

    # ID add
    # I could do like in MMOs and add prefixes and suffixes eg "small x", "huge y"
    # Apple status; dirty = 0.8 * statVal ? ;)

    # https://www.hy-vee.com/recipes-ideas/advice-how-tos/food-love/fall/different-types-of-apples

    def __init__(self):
        appleList = [
            "Granny Smith",
            "Honeycrisp",
            "Pink lady",
            "Jazz",
            "SweeTango",
            "Red delicious",
            "Pinata",
            "Braeburn",
            "Golden delicious",
            "Haralson",
            "Fuji"
        ]
        appleColorList = {
            "Granny Smith": "Green",
            "Honeycrisp": "Red-green",
            "Pink lady": "Pink",
            "Jazz": "Red-green",
            "SweeTango": "Red",
            "Red delicious": "Maroon",
            "Pinata": "Red-green",
            "Braeburn": "Red",
            "Golden delicious": "Yellow-green",
            "Haralson": "Red",
            "Fuji": "Red"
        }
        appleTasteList = {
            "Granny Smith": "Sourish",
            "Honeycrisp": "Sweet",
            "Pink lady": "Tangy",
            "Jazz": "Juicy",
            "SweeTango": "Sweet",
            "Red delicious": "Sweet-sour",
            "Pinata": "Tart",
            "Braeburn": "Sweet",
            "Golden delicious": "Sweet",
            "Haralson": "Tart",
            "Fuji": "Sweet"
        }

        # Picks an apple at random!
        appleName = random.choice(appleList)

        self.inGameName = appleName
        self.weight = random.randrange(50, 250) # Grams
        self.color = appleColorList[ appleName ]
        self.taste = appleTasteList[ appleName ]
        self.texture = "Smooth"
        self.cat = "Apple"
        self.statType = "Food"
        weightToHP = 0.10 # <- Might require future balancing
        self.statVal = round(self.weight * weightToHP, 0)

class Note(Object):

    # ID add
    # Add more variety

    def __init__(self, contents):
        self.inGameName = "Note"
        self.weight = random.randrange(1, 20) # Grams
        self.color = "White"
        self.taste = "Paper"
        self.texture = "Wrinkled"
        self.cat = "Note"
        self.contents = contents
        self.statType = "Int"
        self.statVal = 0

class WeightDisc(Object):

    # ID ADD
    # Add more variety

    def __init__(self):
        self.inGameName = "Weight disc"
        self.weight = random.randrange(1000, 25000) # Grams
        self.color = "Black"
        self.taste = "Rubbery"
        self.texture = "Perfection"
        self.cat = "Weight disc"
        self.statType = "Str"
        weightToStr = 0.0010  # <- *Will* require future balancing; linear, no account for player's stats
        self.statVal = round(self.weight * weightToStr, 0)

# Write a function to automate the generation of start items?
    # Perhaps useful in the generation of the room?

#weightDisc = Object("Weight disc", 1000, "black", "Pig iron", "smooth", "Fitness", "Str")
