class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")
        
class StartTile(MapTile):
    def intro_text(self):
        return """
        You are in a space ship that seems to be completely abandoned. Space pods have been used to flee and the lights flicker. You can go Suddenly, a voice comes over the PA system: Can anyone hear me? Hello? This is your captain speaking. The artificial intellegence has mutinied. Please send help.
        """
    
class BrigHallwayTile(MapTile):
    def intro_text(self):
        return """
        You are in a hallway around the cells in the brig. You can see there are 4 cells, all have been broken out of.
        """
    
class BrigTileOne(MapTile):
    def intro_text(self):
        return """
        You are in Cell One.
        """
    
class BrigTileTwo(MapTile):
    def intro_text(self):
        return """
        You are in Cell Two.
        """
    
class BrigTileThree(MapTile):
    def intro_text(self):
        return """
        You are in Cell Three.
        """
    
class BrigTileFour(MapTile):
    def intro_text(self):
        return """
        You are in Cell Four.
        """
    
class PortHallwayTile(MapTile):
    def intro_text(self):
        return """
        You are in a hallway between the ports. Alien ships are starting to dock as the defenses have been shut off.
        """
    
class PortOneTile(MapTile):
    def intro_text(self):
        return """
        You are in Port One.
        """
    
class PortTwoTile(MapTile):
    def intro_text(self):
        return """
        You are in Port Two.
        """
    
class PortThreeTile(MapTile):
    def intro_text(self):
        return """
        You are in Port Three.
        """
    
class PortFourTile(MapTile):
    def intro_text(self):
        return """
        You are in Port Four.
        """
    
class PortFiveTile(MapTile):
    def intro_text(self):
        return """
        You are in Port Five.
        """
    
class PortSixTile(MapTile):
    def intro_text(self):
        return """
        You are in Port Six.
        """
    
class PortSevenTile(MapTile):
    def intro_text(self):
        return """
        You are in Port Seven.
        """
    
class PortEightTile(MapTile):
    def intro_text(self):
        return """
        You are in Port Eight.
        """
    
class BridgeHallwayTile(MapTile):
    def intro_text(self):
        return """
        You are in a hallway around the bridge.
        """
    
class BridgeHallOne(BridgeHallwayTile):
    def intro_text(self):
        return """
        You can go left or right.
        """
    
class BridgeHallTwo(BrigHallwayTile):
    def intro_text(self):
        return """
        You can go left or right.
        """
    
class BridgeHallThree(BrigHallwayTile):
    def intro_text(self):
        return """
        You can go forward or backwards.
        """
    
class BridgeTile(MapTile):
    def intro_text(self):
        return """
        You are on the bridge. The system controls have been shut off, but you can see there are 6 sections.
        """
    
class BridgeTileOne(MapTile):
    def intro_text(self):
        return """
        You are in the first section.
        """
    
class BridgeTileTwo(MapTile):
    def intro_text(self):
        return """
        You are in the second section.
        """
    
class BridgeTileThree(MapTile):
    def intro_text(self):
        return """
        You are in the third section.
        """
    
class BridgeTileFour(MapTile):
    def intro_text(self):
        return """
        You are in the fourth section.
        """
    
class BridgeTileFive(MapTile):
    def intro_text(self):
        return """
        You are in the fifth section.
        """
    
class BridgeTileSix(MapTile):
    def intro_text(self):
        return """
        You are in the sixth section.
        """
    
class VictoryTile(MapTile):
    def intro_text(self):
        return """
        You get in the escape pod and make it to a nearby planet. Help is on the way to your ship and your captain.
        """

class InfirmaryTile(MapTile):
    def intro_text(self):
        return """
        You are in the infirmary. You can go right, left, or forward.
        """
    
class ArmoryTile(MapTile):
    def intro_text(self):
        return """
        You are in the Armory. You there are plasma rays and lightsaber. You can go right, left, or forward.
        """
    
class CafeteriaTile(MapTile):
    def intro_text(self):
        return """
        You are in the Cafeteria.
        """
    
class GymTile(MapTile):
    def intro_text(self):
        return """
        You are in the Gym.
        """
    
class KitchenTile(MapTile):
    def intro_text(self):
        return """
        You are in the Kitchen.
        """
class FreezerTile(MapTile):
    def intro_text(self):
        return """
        You are in the Freezer. Best hope it doesn't lock.
        """
    
class BathroomTile(MapTile):
    def intro_text(self):
        return """
        You are in the Bathroom.
        """
    
class MeetingRoomTile(MapTile):
    def intro_text(self):
        return """
        You are in the Meeting Room
        """
    
class BedroomTile(MapTile):
    def intro_text(self):
        return """
        You are in the Bedroom.
        """
    
class LaundryTile(MapTile):
    def intro_text(self):
        return """
        You are in the Laundry Room.
        """
    
class StorageTile(MapTile):
    def intro_text(self):
        return """
        You are in the Storage closet.
        """
    

    
class ShowersTile(MapTile):
    def intro_text(self):
        return """
        You are in the Showers.
        """
    
class SuitStorageTile(MapTile):
    def intro_text(self):
        return """
        You are in the suit storage closet.
        """
    
class PodHallTile(MapTile):
    def intro_text(self):
        return """
        You are in the hallway to the escape pods.
        """
    
class GenericHallTile(MapTile):
    def intro_text(self):
        return """
        You are in a hallway.
        """
    
ship_map = [
    [VictoryTile(0, 0),PodHallTile(1, 0),SuitStorageTile(2, 0), LaundryTile(3, 0),ShowersTile(4, 0),StorageTile(5,0), StorageTile(6,0), BathroomTile(7,0), None,None],
    [BedroomTile(0,1),None,None,None,ShowersTile(4, 1),LaundryTile(5,1),GenericHallTile(6,1),GenericHallTile(7,1),BedroomTile(8,1),None],
    [KitchenTile(0,2),FreezerTile(1,2),None,BathroomTile(3,2),None,GenericHallTile(5,2),None,None, None, FreezerTile(9, 2)],
    [CafeteriaTile(0, 3),None, None, BrigHallwayTile(3,4), BrigHallwayTile(4, 3), BrigHallwayTile(5, 3), BrigHallwayTile(6, 3),None, FreezerTile(8,3),KitchenTile(9,3)],
    [GymTile(0, 4),MeetingRoomTile(1, 4), MeetingRoomTile(2,4),BrigHallwayTile(3,4),BrigTileOne(4, 4),BrigTileTwo(5, 4), BrigHallwayTile(6, 4), None,None,CafeteriaTile(9, 4)],
    [None,BrigHallwayTile(1, 5),BrigHallwayTile(2,5), BrigHallwayTile(3, 5),BrigTileThree(4, 5),BrigTileFour(5, 5), BrigHallwayTile(6, 5),BrigHallwayTile(7, 5),PortHallwayTile(8,5), PortFourTile(9, 5)],
    [PortEightTile(0, 6), PortHallwayTile(1, 6),None,BrigHallwayTile(3,6),BrigHallwayTile(4,6), BrigHallwayTile(5,6), BrigHallwayTile(6,6), BrigHallwayTile(7,6), PortHallwayTile(8, 6), PortThreeTile(9,7)],
    [PortSevenTile(0,7),PortHallwayTile(1,7),None,None, BridgeHallThree(4, 7),None,BedroomTile(6,7),None, PortHallwayTile(8, 7),PortTwoTile(9, 7)],
    [PortSixTile(0, 8),PortHallwayTile(1,8),BathroomTile(2, 8), BridgeTileOne(3, 8),BridgeTileTwo(4, 8),BridgeTileThree(5,8),None,None, PortHallwayTile(8, 8),PortOneTile(9, 8)],
    [PortFiveTile(0, 9),PortHallwayTile(1,9),BridgeHallTwo(2, 9), BridgeTileFour(3, 9),BridgeTileFive(4, 9),BridgeTileSix(5,9),BridgeHallOne(6, 9), ArmoryTile(7, 9),InfirmaryTile(8, 9), StartTile(9, 9)],
]

def tile_at(x,y):
    if x<0 or y<0:
        return None
    try:
        return ship_map[y][x]
    except IndexError:
        return None
    