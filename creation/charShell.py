# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 12:04:31 2016
@author: Jakob Papirov

    Add randomised stats; check paper notes
    Add a 'hidden' health start value to be used for calc'ing the dmg
"""



class Character:

    def __init__(self):

        # Self
        self.name = ""
        self.location = ""

        # Body
        self.heads = 0
        self.eyes = 0
        self.ears = 0
        self.arms = 0
        self.legs = 0
        self.butts = 0
        self.genitalia = 0

        # Stats
        self.int = 0
        self.str = 0

        # Meta stats
        self.health = 100

        charSelf = {
            "name": self.name,
        }

        charSelfLoc = {
            "location": self.location
        }

        charBody = {
            "heads": self.heads,
            "eyes": self.eyes,
            "arms": self.arms,
            "ears": self.ears,
            "legs": self.legs,
            "butts": self.butts,
            "genitalia": self.genitalia
        }

        charStats = {
            "int": self.int,
            "str": self.str
        }

        charStatsMeta = {
            "health": self.health
        }

class Human(Character):

    def generateHuman(self, charName):

        # Body
        self.heads = 1
        self.ears = 2
        self.eyes = 2
        self.arms = 2
        self.legs = 2
        self.butts = 1
        self.genitalia = 1

        # Stats
        self.int = 5
        self.str = 5

        # Meta stats
        self.health = 100

        # Self
        charSelf = charName  # From input, createChar
        # Is currently a hack, as I really wanted one dictionary, but unable to access/set vals
        charSelfLoc = "The void"

        charBody = {
            "heads": self.heads,
            "ears": self.ears,
            "eyes": self.eyes,
            "arms": self.arms,
            "legs": self.legs,
            "butts": self.butts,
            "genitalia": self.genitalia
        }

        charStats = {
            "int": self.int,
            "str": self.str
        }

        charStatsMeta = {
            "health": self.health
        }

        # https://www.programiz.com/python-programming/nested-dictionary
        char = {
            "charBody": charBody,
            "charStats": charStats,
            "charStatsMeta": charStatsMeta,
            "charSelf": charSelf,
            "charSelfLoc": charSelfLoc
        }

        return char
