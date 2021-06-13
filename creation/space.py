# Not working as intended
# Doesn't print the location or doors (self)
# Should the room have info of nr of objects inside it? types etc? total weight lol


class Space:
    walls = 0
    windows = 0

    def __init__(self):
        self.gravity = 1.0
        self.locationID = 0
        self.doors = 0

class Room(Space):
    walls = 6

    def __init__(self, name, doors, windows): # doors = INT
        self.name = name
        self.doors = doors
        self.windows = windows

    def roomInfo(self):
        print("Room name: ", self.name)
        print("# Doors: ", self.doors)
        print("# Windows: ", self.windows)
        print("Walls: ", Room.walls)

class Building(Space):
    walls = 6


    def __init__(self, buildingName, maxRooms, room=None):
        self.buildingName = buildingName
        self.maxRooms = maxRooms
        if room is None:
            self.rooms = []
        else:
            self.rooms = room

    def add_room(self, room):
        if room not in self.rooms:
            self.rooms.append(room)

    def remove_room(self, room):
        if room not in self.rooms:
            self.rooms.remove(room)

    def buildingInfo(self):
        print("BuildingName: ", self.buildingName)
        print("Max rooms: ", self.maxRooms)
        for room in self.rooms:
            print("Room: ", room) # Not as intended

class Door:

    def __init__(self, thickness, lockType, doorMaterial):
        self.thickness = thickness
        self.lockType = lockType
        self.doorMaterial = doorMaterial

    def doorInfo(self):
        print("Door thickness: ", self.thickness, " cm")
        print("Door lock type: ", self.lockType)
        print("Door material: ", self.doorMaterial)

#spawn = Room("Spawn", 1) # Works
#spawn.roomInfo() # Works

#hallway = Room("Hallway", 3)
#hallway.roomInfo()

#spawnDoor = Door(5, "Knob lock", "Mahogany") # Works
#spawnDoor.doorInfo() # Works

#firstBuilding = Building("01", 18, [spawn]) # Not as expected
#firstBuilding.buildingInfo()
