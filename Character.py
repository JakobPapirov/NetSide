# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 12:04:31 2016

@author: Jakob
"""
import random


class Character:  # Har precis skapat en tom karaktär!

    def __init__(self):
        # Body
        self.charEmptyBody = {
            "Heads": 0,
            "Eyes": 0,
            "Arms": 0,
            "Legs": 0,
            "Ears": 0
        }
        self.test = 1
        self.Heads = 0  # Change to dictionary syntax->problems
        self.Eyes = 0
        self.Arms = 0
        self.Legs = 0
        self.Ears = 0
        # Stats
        charEmptyStats = {
            "Int": 0,
            "Agi": 0,
            "Str": 0
        }
        self.Int = 0
        self.Agi = 0
        self.Str = 0
        # Just nu kan man inte lägga statpoints på liv och en karaktär har
        # inte mer start hp.
        Vit = 20
        vitFactor = 5
        charEmptyStatsMeta = {
            "Vit": Vit,
            "Health": Vit * vitFactor,
            "Stamina": 100,
            "Focus": 100,
            "Stats": 20
        }  # Focus, vit and stamina should be influenced by stats; like int and
        # focus
        self.Vit = 20
        self.Health = self.Vit * vitFactor
        self.Stamina = 100
        self.Focus = 100
        self.Stats = 20  # Number of initial stat points

    def eat(self):
        # Health Check
        if self.Health >= 100 or self.Focus >= 100:
#        if charEmptyStats["Health"] >= 100 or charEmptyStats["Focus"] >= 100:
            print("You already have full health.")
        else:  # Add things that can go wrong
            self.Health += 5
            self.Focus += 5
            print("Health now at {} and focus at {}.".format(self.Health))

    def workOutStr(self):  # Create different types later
        # Something good may happen during working out
        RandBoost = random.randint(1, 100)  # add int check below
        if self.Str <= 20:  # Str check for probability
            if RandBoost <= 40:  # 40 % chance
                self.Str += 2
                print("What a great workout session, you've gained extra \
stength!")
                print("You now have {} strength".format(self.Str))
            else:
                pass
        elif self.Str <= 75:  # Str check for probability
            if RandBoost <= 20:  # 20 % chance
                self.Str += 2
                print("What a great workout session, you've gained extra \
stength!")
                print("You now have {} strength".format(self.Str))
            else:
                pass
        else:
            pass
        # Something bad may happen during working out
        RandOuch = random.randint(1, 100)
        if self.Str <= 50 and self.Str <= 100:  # Str check for probability
            if RandOuch <= 20:  # 20 % risk
                self.Str -= 5
                print("Ouch, you hurt yourself, you've lost stength!")
                print("You now have {} strength".format(self.Str))
            else:
                pass
        elif self.Str > 100:  # Str check for probability
            if RandOuch == 1:  # 1 % risk
                self.Str -= 5
                print("Ouch, you hurt yourself, you've lost stength!")
                print("You now have {} strength".format(self.Str))
            else:
                pass
        else:
            pass
        # Does the actual workout
        if self.Int <= 1:  # Int check
            print("You don't have enough Int to do that!")
        else:
            if self.Stamina > 0:
                self.Str += 1
                self.Stamina -= 5
                print("You now have {} strength and {} \
stamina".format(self.Str, self.Stamina))
            else:
                    print("You are exhausted from the work-out!")

    def workOutInt(self):
        if self.Focus > 0:
            IntQa = random.randint(0, 10)
            IntQb = random.randint(0, 10)
            IntA = IntQa + IntQb
            InpA = int(input("What is the sum of " + str(IntQa) + " and " +
                             str(IntQb) + "? "))
            if InpA == IntA:
                self.Int += 1  # Add IntBoost
                self.Focus -= 5
                print("Yes, you are correct!")
                print("You now have {} int and {} \
focus".format(self.Int, self.Focus))
            else:
                print("The answer was " + str(IntA))
                print("Oh no, that's not right!")  # Discover Sandra class!
        else:
            print("You are exhausted from all the problem solving!")


class Human(Character):

    def Generate(self):
        # Body
        self.Heads = 1
        self.Eyes = 2
        self.Arms = 2
        self.Legs = 2
        self.Ears = 2
        # Stats
        #  placestats doesn't listen to local values
        self.Int = 5
        self.Agi = 5
        self.Str = 5
        # Change to .format(self.x) later
        print("You have created a human with:")
        print("One (1) head")
        print("Two (2) eyes")
        # add +vision due to two eyes and color vision
        print("Two (2) arms")
        print("Two (2) ears")
        print("Two (2) legs")


class Sandra(Human):  # we are subsets of human characters.

    def Generate(self):
        # Stats
        #  placestats doesn't listen to local values; perhaps
        #  a function is required, with input being self.Int or Int
        self.Int = 10
        self.Agi = 2
        self.Str = 2
# add languages and qty language bonus


class Jakob(Human):  # we are subsets of human characters.

    def Generate(self):
        # Stats
        #  placestats doesn't listen to local values; perhaps
        #  a function is required, with input being self.Int or Int
        self.Agi = 5
        self.Str = 10
# add languages and qty language bonus
# humans have males/females
