"""
    Generate possible doors and possible SPAWN doors
"""


import sys
sys.path.insert(0, './creation')
from creation.space import Room, Door

# WORKS! 21-06-11

def spawnRoom():
    # syntax = Room("name", #doors, #windows
    spawn = Room("Spawn", 1, 2)

    # Dev-purposes
    #spawn.roomInfo()

    # https://securitysnobs.com/Types-Of-Locks.html
    spawnDoor = Door(5, "Knob lock", "Mahogany")

    # Dev-purposes
    #spawnDoor.doorInfo()

    # Perhaps return generated objects as well; reqs import objects.py

    return spawn, spawnDoor
