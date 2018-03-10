from random import randint
import spaceitems
import spaceenemies
import barriers
import spaceplayer

class MapTile:
	description= "Do not create raw MapTiles! Create a subclass instead!"
	barriers = []
	enemies = []
	items = []
	npcs = []
    
	def random_spawn(self):
		if(randint(0,3)==0):
			self.enemies = [spaceenemies.Greebybobe()]
		else:
			self.enemies = []
	def random_spawn(self):
		if(randint(0,3)==0):
			self.enemies = [spaceenemies.TelepathicSpider()]
		else:
			self.enemies = [] 
	def random_spawn(self):
		if(randint(0,3)==0):
			self.enemies = [spaceenemies.FFloopian()]
		else:
			self.enemies = [] 
            
	def __init__(self, x=0, y=0, barriers = [], items = [], enemies = [], npcs = []):
		self.x = x
		self.y = y
		for barrier in barriers:
			self.add_barrier(barrier)
		for item in items:
			self.add_item(item)
		for enemy in enemies:
			self.add_enemy(enemy)
		for npc in npcs:
			self.add_npc(npc)
            
	def intro_text(self):
		text = self.description
		directions_blocked = []
		
		for enemy in self.enemies:
			#if (enemy.direction):
				#if(enemy.direction not in directions_blocked):
				#	directions_blocked.append(enemy.direction)
			text += " " + enemy.check_text()
		for barrier in self.barriers:
			if (barrier.direction):
				if(barrier.direction not in directions_blocked):
					if(barrier.verbose):
						text += " " + barrier.description()
		for npc in self.npcs:
			text += " " + npc.check_text()
		for item in self.items:
			text += """ 
            - """ + item.check_text()

		return text
		
	def handle_input(self, verb, noun1, noun2, inventory):
		if(not noun2):
			if(verb == 'check'):
				for barrier in self.barriers:
					if(barrier.name):
						if(barrier.name.lower() == noun1):
							return [True, barrier.description(), inventory]
				for item in self.items:
					if(item.name.lower() == noun1):
						return [True, item.check_text(), inventory]
				for enemy in self.enemies:
					if(enemy.name.lower() == noun1):
						return [True, enemy.check_text(), inventory]
				for npc in self.npcs:
					if(npc.name.lower() == noun1):
						return [True, npc.check_text(), inventory]
			elif(verb == 'take'):
				for index in range(len(self.items)):
					if(self.items[index].name.lower() == noun1):
						if(isinstance(self.items[index], spaceitems.Item)):
							pickup_text = "You picked up the %s." % self.items[index].name
							inventory.append(self.items[index])
							self.items.pop(index)
							return [True, pickup_text, inventory]
						else:
							return [True, "The %s is too heavy to pick up." % self.items[index].name, inventory]
			elif(verb == 'drop'):
				for index in range(len(inventory)):
					if(inventory[index].name.lower() == noun1):
						inventory[index].is_dropped = True
						drop_text = "You dropped the %s." % inventory[index].name
						self.add_item(inventory[index])
						inventory.pop(index)
						return [True, drop_text, inventory]

		for list in [self.barriers, self.items, self.enemies, self.npcs]:
			for item in list:
				[status, description, inventory] = item.handle_input(verb, noun1, noun2, inventory)
				if(status):
					return [status, description, inventory]
					
		for list in [self.barriers, self.items, self.enemies, self.npcs]:			# Added to give the player feedback if they have part of the name of an object correct.
			for item in list:
				if(item.name):
					if(noun1 in item.name):
						return [True, "Be more specific.", inventory]
			
		return [False, "", inventory]
		
	def add_barrier(self, barrier):
		if(len(self.barriers) == 0):
			self.barriers = [barrier]		# Initialize the list if it is empty.
		else:
			self.barriers.append(barrier)	# Add to the list if it is not empty.
			
	def add_item(self, item):
		if(len(self.items) == 0):
			self.items = [item]		# Initialize the list if it is empty.
		else:
			self.items.append(item)	# Add to the list if it is not empty.
			
	def add_enemy(self, enemy):
		if(len(self.enemies) == 0):
			self.enemies = [enemy]		# Initialize the list if it is empty.
		else:
			self.enemies.append(enemy)	# Add to the list if it is not empty.
			
	def add_npc(self, npc):
		if(len(self.npcs) == 0):
			self.npcs = [npc]		# Initialize the list if it is empty.
		else:
			self.npcs.append(npc)	# Add to the list if it is not empty.
			
	def random_spawn(self):
		pass						# Update this for your specific subclass if you want randomly spawning enemies.
			
	def update(self, player):
		dead_enemy_indices = []
		for index in range(len(self.enemies)):
			if (not self.enemies[index].is_alive()):
				dead_enemy_indices.append(index)
				for item in self.enemies[index].loot:
					self.add_item(item)
		for index in reversed(dead_enemy_indices):
			self.enemies.pop(index)
		if(self.x == player.x and self.y == player.y):
			for enemy in self.enemies:
				if(enemy.agro):
					agro_text = "The %s seems very agitated. It attacks! " % enemy.name
					agro_text += player.take_damage(enemy.damage)
					print()
					print(agro_text)
        
        
class StartTile(MapTile):
    description= """
        You are in a space ship that seems to be completely abandoned. Space pods have been used to flee and the lights flicker. Suddenly, a voice comes over the PA system: Can anyone hear me? Hello? This is your captain speaking. The artificial intellegence has mutinied. Please send help.
        You can go left or forward. The directions are as follows:
                ^  Forward   <  Left   > Right   \/ Backwards
        """
class BrigHallwayTile(MapTile):
    description= """
        You are in a hallway around the cells in the brig. You can see there are 4 cells, all have been broken out of.
        """
    def random_spawn(self):
        if(randint(0,3)==0):
            self.enemies = [spaceenemies.Gromflamite()]
        else:
            self.enemies = []
    
class BrigTileOne(MapTile):
    description= """
        You are in Cell One.
        """
    def random_spawn(self):
        if(randint(0,3)==0):
            self.enemies = [spaceenemies.Gazorpian()]
        else:
            self.enemies = []
            
class BrigTileTwo(MapTile):
    description= """
        You are in Cell Two.
        """
    def random_spawn(self):
        if(randint(0,3)==0):
            self.enemies = [spaceenemies.Gazorpian()]
        else:
            self.enemies = []
            
class BrigTileThree(MapTile):
    description= """
        You are in Cell Three.
        """
    def random_spawn(self):
        if(randint(0,3)==0):
            self.enemies = [spaceenemies.Gazorpian()]
        else:
            self.enemies = []
            
class BrigTileFour(MapTile):
    description= """
        You are in Cell Four.
        """
    def random_spawn(self):
        if(randint(0,3)==0):
            self.enemies = [spaceenemies.Gazorpian()]
        else:
            self.enemies = []
            
class PortHallwayTile(MapTile):
    description= """
        You are in a hallway between the ports. Alien ships are starting to dock as the defenses have been shut off.
        """
    
class PortOneTile(MapTile):
    description= """
        You are in Port One.
        """
    def random_spawn(self):
        if(randint(0,3)==0):
            self.enemies = [spaceenemies.GearPerson()]
        else:
            self.enemies = []
    def random_spawn(self):
        if(randint(0,3)==1):
            self.enemies = [spaceenemies.TelepathicSpider()]
        else:
            self.enemies = []
            
class PortTwoTile(MapTile):
    description= """
        You are in Port Two.
        """
    def random_spawn(self):
        if(randint(0,3)==0):
            self.enemies = [spaceenemies.GearPerson()]
        else:
            self.enemies = []
    def random_spawn(self):
        if(randint(0,3)==1):
            self.enemies = [spaceenemies.TelepathicSpider()]
        else:
            self.enemies = []
            
class PortThreeTile(MapTile):
    description= """
        You are in Port Three.
        """
    def random_spawn(self):
        if(randint(0,3)==0):
            self.enemies = [spaceenemies.GearPerson()]
        else:
            self.enemies = []
    def random_spawn(self):
        if(randint(0,3)==1):
            self.enemies = [spaceenemies.TelepathicSpider()]
        else:
            self.enemies = []
            
class PortFourTile(MapTile):
    description= """
        You are in Port Four.
        """
    def random_spawn(self):
        if(randint(0,3)==0):
            self.enemies = [spaceenemies.GearPerson()]
        else:
            self.enemies = []
    def random_spawn(self):
        if(randint(0,3)==1):
            self.enemies = [spaceenemies.TelepathicSpider()]
        else:
            self.enemies = []
class PortFiveTile(MapTile):
    description= """
        You are in Port Five.
        """
    def random_spawn(self):
        if(randint(0,3)==0):
            self.enemies = [spaceenemies.GearPerson()]
        else:
            self.enemies = []
    def random_spawn(self):
        if(randint(0,3)==1):
            self.enemies = [spaceenemies.TelepathicSpider()]
        else:
            self.enemies = []  
class PortSixTile(MapTile):
    description= """
        You are in Port Six.
        """
    def random_spawn(self):
        if(randint(0,3)==0):
            self.enemies = [spaceenemies.GearPerson()]
        else:
            self.enemies = []
    def random_spawn(self):
        if(randint(0,3)==1):
            self.enemies = [spaceenemies.TelepathicSpider()]
        else:
            self.enemies = []        
class PortSevenTile(MapTile):
    description= """
        You are in Port Seven.
        """
    def random_spawn(self):
        if(randint(0,3)==0):
            self.enemies = [spaceenemies.GearPerson()]
        else:
            self.enemies = []
    def random_spawn(self):
        if(randint(0,3)==1):
            self.enemies = [spaceenemies.TelepathicSpider()]
        else:
            self.enemies = []        
class PortEightTile(MapTile):
    description= """
        You are in Port Eight.
        """
    def random_spawn(self):
        if(randint(0,3)==0):
            self.enemies = [spaceenemies.GearPerson()]
        else:
            self.enemies = []
    def random_spawn(self):
        if(randint(0,3)==1):
            self.enemies = [spaceenemies.TelepathicSpider()]
        else:
            self.enemies = []
class BridgeHallwayTile(MapTile):
    description= """
        You are in a hallway around the bridge.
        """
    def random_spawn(self):
        if(randint(0,3)==1):
            self.enemies = [spaceenemies.Gromflamite()]
        else:
            self.enemies = []
			
class BridgeHallOne(MapTile):
    description= """
        You are in the hallway to the bridge. You can go left or right.
        """
    def random_spawn(self):
        if(randint(0,3)==1):
            self.enemies = [spaceenemies.Gromflamite()]
        else:
            self.enemies = []
			
class BridgeHallTwo(MapTile):
    description= """
        You are in the hallway to the bridge. You can go left or right.
        """
    def random_spawn(self):
        if(randint(0,3)==1):
            self.enemies = [spaceenemies.Gromflamite()]
        else:
            self.enemies = []
			
class BridgeHallThree(MapTile):
    description= """
        You are in the hallway to the bridge. You can go forward or backwards.
        """
    def random_spawn(self):
        if(randint(0,3)==1):
            self.enemies = [spaceenemies.Gromflamite()]
        else:
            self.enemies = []
			
class BridgeTile(MapTile):
    description= """
        You are on the bridge. The system controls have been shut off, but you can see there are 6 sections.
        """
    def random_spawn(self):
        if(randint(0,3)==1):
            self.enemies = [spaceenemies.Gromflamite()]
        else:
            self.enemies = []
			
class BridgeTileOne(MapTile):
    description= """
        You are in the first section of the bridge.
        """
    def random_spawn(self):
        if(randint(0,3)==1):
            self.enemies = [spaceenemies.Gromflamite()]
        else:
            self.enemies = []
			
class BridgeTileTwo(MapTile):
    description= """
        You are in the second section of the bridge.
        """
    def random_spawn(self):
        if(randint(0,3)==1):
            self.enemies = [spaceenemies.Gromflamite()]
        else:
            self.enemies = []
			
class BridgeTileThree(MapTile):
    description= """
        You are in the third section of the bridge.
        """
    def random_spawn(self):
        if(randint(0,3)==1):
            self.enemies = [spaceenemies.Gromflamite()]
        else:
            self.enemies = []
			
class BridgeTileFour(MapTile):
    description= """
        You are in the fourth section of the bridge.
        """
    def random_spawn(self):
        if(randint(0,3)==1):
            self.enemies = [spaceenemies.Gromflamite()]
        else:
            self.enemies = []
			
class BridgeTileFive(MapTile):
    description= """
        You are in the fifth section of the bridge.
        """
    def random_spawn(self):
        if(randint(0,3)==1):
            self.enemies = [spaceenemies.Gromflamite()]
        else:
            self.enemies = []
			
class BridgeTileSix(MapTile):
    description= """
        You are in the sixth section of the bridge.
        """
    items = [spaceitems.PodKey()]
	
    def random_spawn(self):
        if(randint(0,3)==1):
            self.enemies = [spaceenemies.Gromflamite()]
        else:
            self.enemies = []
			
class VictoryTile(MapTile):
    description= """
        You get in the escape pod and make it to a nearby planet. Help is on the way to your ship and your captain.
        """

class InfirmaryTile(MapTile):
    description= """
        You are in the infirmary. You can go right, left, or forward.
        """
    items = [spaceitems.Gauze(), spaceitems.IcePack(), spaceitems.BandAid()]
    
class ArmoryTile(MapTile):
    description= """
        You are in the Armory. You can go right, left, or forward.
        """
    items = [spaceitems.PlasmaRay(), spaceitems.Lightsaber()]
    
class CafeteriaTile(MapTile):
    description= """
        You are in the Cafeteria.
        """
    items = [spaceitems.SpaceCream(), spaceitems.SpaceSandwich()]
    
class GymTile(MapTile):
    description= """
        You are in the Gym.
        """
    
class KitchenTile(MapTile):
    description= """
        You are in the Kitchen.
        """
    items = [spaceitems.SpaceCarrots(), spaceitems.SpaceSoda()]
	
class FreezerTile(MapTile):
    description= """
        You are in the Freezer.
        """
    def update(self, player):
        dead_enemy_indices = []
        for index in range(len(self.enemies)):
            if (not self.enemies[index].is_alive()):
                dead_enemy_indices.append(index)
                for item in self.enemies[index].loot:
                    self.add_item(item)
        for index in reversed(dead_enemy_indices):
            self.enemies.pop(index)
        if(self.x == player.x and self.y == player.y):		# Add some kind of counter here to determine how long the player has been in the freezer.
            for enemy in self.enemies:
                if(enemy.agro):
                    agro_text = "The %s seems very aggitated. It attacks! " % enemy.name
                    agro_text += player.take_damage(enemy.damage)
                    print()
                    print(agro_text)
                    
    def random_spawn(self):
        if(randint(0,1)==0):
            if(self.x == 9):
                self.barriers = [barriers.FreezerDoor('r')]
            elif(self.x == 2):
                self.barriers = [barriers.FreezerDoor('l')]
        else:
            print("The AI might lock it soon.")

class BathroomTile(MapTile):
    description= """
        You are in the Bathroom.
        """
    def random_spawn(self):
        if(randint(0,3)==1):
            self.enemies = [spaceenemies.FFloopian()]
        else:
            self.enemies = []
			
class MeetingRoomTile(MapTile):
    description= """
        You are in the Meeting Room
        """
    def random_spawn(self):
        if(randint(0,3)==1):
            self.enemies = [spaceenemies.GreebyBobes()]
        else:
            self.enemies = []
			
class BedroomTile(MapTile):
    description= """
        You are in the Bedroom.
        """
    
class LaundryTile(MapTile):
    description= """
        You are in the Laundry Room.
        """
    
class StorageTile(MapTile):
    description= """
        You are in the Storage closet.
        """
    def random_spawn(self):
        if(randint(0,3)==1):
            self.enemies = [spaceenemies.FFloopian()]
        else:
            self.enemies = []
			
class ShowersTile(MapTile):
    description= """
        You are in the Showers.
        """
    
class SuitStorageTile(MapTile):
    description= """
        You are in the suit storage closet.
        """
	
    def random_spawn(self):
        if(0==0):
            self.barriers = [barriers.PodDoor('l')]
            
class PodHallTile(MapTile):
    description= """
        You are in the hallway to the escape pods.
        """
	
class GenericHallTile(MapTile):
    description= """
        You are in a hallway.
        """
	
class World:
    ship_map = [
        [None, None, None, None, None, None, None, None, None, None, None, None],
        [None, VictoryTile(1, 1),PodHallTile(2, 1),SuitStorageTile(3, 1), LaundryTile(4, 1),ShowersTile(5, 1),StorageTile(6,1), StorageTile(7,1), BathroomTile(8,1), None,None, None],
        [None, BedroomTile(1,2),None,None,None,ShowersTile(5, 2),LaundryTile(6,2),GenericHallTile(7,2),GenericHallTile(8,2),BedroomTile(9,2),None,None],
        [None, KitchenTile(1,3),FreezerTile(2,3),None,BathroomTile(4,3),None,GenericHallTile(7,3),None,None, None, None, None],
        [None, CafeteriaTile(1, 4),None, None, BrigHallwayTile(4,4), BrigHallwayTile(5, 4), BrigHallwayTile(6, 4), BrigHallwayTile(7, 4),None, FreezerTile(9,4),KitchenTile(10,4), None],
        [None, GymTile(1, 5),MeetingRoomTile(2, 5), MeetingRoomTile(3,5),BrigHallwayTile(4,5),BrigTileOne(5, 5),BrigTileTwo(6, 5), BrigHallwayTile(7, 5), None,None,CafeteriaTile(10, 5), None],
        [None, None,BrigHallwayTile(2, 6),BrigHallwayTile(3,6), BrigHallwayTile(4, 6),BrigTileThree(5, 6),BrigTileFour(6, 6), BrigHallwayTile(7, 6),BrigHallwayTile(8, 6),PortHallwayTile(9,6), PortFourTile(10, 6), None],
        [None, PortEightTile(1, 7), PortHallwayTile(2, 7),None,BrigHallwayTile(4,7),BrigHallwayTile(5,7), BrigHallwayTile(6,7), BrigHallwayTile(7,7), BrigHallwayTile(8,7), PortHallwayTile(9, 7), PortThreeTile(10,7), None],
        [None, PortSevenTile(1,8),PortHallwayTile(2,8),None,None, BridgeHallThree(5, 8),None,BedroomTile(7,8),None, PortHallwayTile(9, 8),PortTwoTile(10, 8), None],
        [None, PortSixTile(1, 9),PortHallwayTile(2,9),BathroomTile(3, 9), BridgeTileOne(4, 9),BridgeTileTwo(5, 9),BridgeTileThree(6,9),None,None, PortHallwayTile(9, 9),PortOneTile(10, 9), None],
        [None, PortFiveTile(1, 10),PortHallwayTile(2, 10),BridgeHallTwo(3, 10), BridgeTileFour(4, 10), BridgeTileFive(5, 10), BridgeTileSix(6,10), BridgeHallOne(7, 10), ArmoryTile(8, 10), InfirmaryTile(9, 10), StartTile(10, 10), None],
        [None, None, None, None, None, None, None, None, None, None, None, None]
    ]

    def tile_at(self,x,y):
        if x<0 or y<0:
            return None
        try:
            return self.ship_map[y][x]
        except IndexError:
            return None


    def check_forward(self, x, y):
        for barrier in self.ship_map[y][x].barriers:
            if(barrier.direction == 'forward' and not barrier.passable):
                return [False, barrier.description()]	

        if y-1 < 0:
            room = None
        try:
            room = self.ship_map[y-1][x]
        except IndexError:
            room = None

        if(room):
            return [True, "You have moved forward"]
        else:
            return [False, "There is a wall there."]
    def check_back(self, x, y):
        for barrier in self.ship_map[y][x].barriers:
            if(barrier.direction == 'back' and not barrier.passable):
                return [False, barrier.description()]

        if y+1 < 0:
            room = None
        try:
            room = self.ship_map[y+1][x]
        except IndexError:
            room = None
                
        if(room):
            return [True, " "]
        else:
            return [False, "There is a wall there."]

    def check_left(self, x, y):
        for barrier in self.ship_map[y][x].barriers:
            if(barrier.direction == 'left' and not barrier.passable):
                return [False, barrier.description()]
        if x-1 < 0:
            room = None
        try:
            room = self.ship_map[y][x-1]
        except IndexError:
            room = None
            
        if(room):
            return [True, " "]
        else:
            return [False, "There is a wall there."]

    def check_right(self, x, y):
        for barrier in self.ship_map[y][x].barriers:
            if(barrier.direction == 'right' and not barrier.passable):
                return [False, barrier.description()]
        if x+1 < 0:
            room = None
        try:
            room = self.ship_map[y][x+1]
        except IndexError:
            room = None
                
        if(room):
            return [True, " "]
        else:
            return [False, "There is a wall there."]
            
    def updateRooms(self, spaceplayer):
        for row in self.ship_map:
            for room in row:
                if(room):
                    room.update(spaceplayer)