from random import randint

class Item:
	name = "Do not creat raw Item objects!"
	description = "define later"
	droppedDescription = "define later"
	
	isDropped = False
	value = 0
	def __init__(self, description="", value = 0):
		if(description):
			self.introDescription = self.description
		else:
			self.introDescription = self.droppedDescription
		if(self.value == 0):
			self.value = value
	def __str__(self):
		return self.name
	def room_text(self):
		if(not self.isDropped):
			return self.introDescription
		else:
			return self.droppedDescription
	def check_text(self):
		return self.name
	def drop(self):
		self.is_dropped = True
	def pickUp(self):
		self.isDropped = False
		
	def handle_input(self, verb, noun1, noun2, inventory):
		return[False, None, inventory]
    
class SpaceFood(Item):
    addedHP = 0
    def consume(self):
        return [self.eatenText, self.addedHP]
    
class SpaceCream(SpaceFood):
	def __init__(self, value = 0):
		self.addedHP = 5
		self.name = "SpaceCream"
		self.description = "A creamy desert."
		self.droppedDescription = "The SpaceCream (tm) you dropped is lying on the floor."
		if(self.value == 0):
			self.value = value
		self.eatenText = "You have eaten the SpaceCream (tm)."
       
        
        
class SpaceSandwich(SpaceFood):
    def __init__(self):
        self.addedHP = 10
        self.name = "SpaceSandwich"
        self.description = "A filling sandwich"
        self.droppedDescription = "The sandwich you dropped is lying on the floor."
        self.eatenText = "You have eaten the sandwich."
        
class SpaceWeapon(Item):	
	equip_description = "You should define flavor text for equipping this item in its subclass."
	attack_descriptions = ["You should define one or more attack descriptions as a list in your subclass.", "This is an example secondary attack description"]

	damage = 0
	def equip_text(self):
		return self.equip_description
			
	def attack(self):
		return [self.attack_descriptions[randint(0, len(self.attack_descriptions)-1)], self.damage]
		

class PlasmaRay(SpaceWeapon):
	equip_description = "You have equipped your plasma ray."
	attack_descriptions = ["You nearly miss.", "You hit right on target!"]
	
	def __init__(self):
		self.name = 'Plasma Ray'
		self.description = 'A trigger activated gun that shoots plasma rays, liquifying the opponents insides.'
		self.droppedDescription = "A gun-like object is on the ground in front of you."
		self.damage = 10
	def __str__(self):
		return "Name: {} Description: {} Damage: {}".format(self.name, self.description, self.damage)
		
class Lightsaber(SpaceWeapon):
	equip_description = "You arm yourself with your lightsaber."
	attack_descriptions = ["The lightsaber swooshes through the air and nearly misses the target.", "You stab directly through your enemy."]
	
	def __init__(self):
		self.name = 'Lightsaber'
		self.description = 'You know exactly what this is.'
		self.droppedDescription = "A lightsaber is on the ground in front of you."
		self.damage = 15
	def __str__(self):
		return "Name: {} Description: {} Damage: {}".format(self.name, self.description, self.damage)
		
class FreezerKey(Item):
	def __init__(self):
		self.name = 'Freezer key'
		self.description = "Keep this; you'll need it later."
		self.droppedDescription = "A cold key is on the ground in front of you."
	def __str__(self):
		return "Name: {} Description: {}".format(self.name, self.description)
    
class PodKey(Item):
	def __init__(self):
		self.name = 'Pod key'
		self.description = "Keep this; you'll need it later."
		self.droppedDescription = "A circular key is on the ground in front of you."
	def __str__(self):
		return "Name: {} Description: {}".format(self.name, self.description)