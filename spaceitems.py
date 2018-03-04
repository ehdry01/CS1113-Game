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
	def roomText(self):
		if(not self.isDropped):
			return self.introDescription
		else:
			return self.droppedDescription
	def checkText(self):
		return self.description
	def drop(self):
		self.isDropped = True
	def pickUp(self):
		self.isDropped = False
	def handleInput(self, verb, noun1, noun2, inventory):
		return[False, None, inventory]

class SpaceWeapon(Item):	
	equip_description = "You should define flavor text for equipping this item in its subclass."
	attack_descriptions = ["You should define one or more attack descriptions as a list in your subclass.", "This is an example secondary attack description"]

	damage = 0		# Define this appropriately in your subclass.
		
	def equip_text(self):
		return self.equip_description
			
	def attack(self):
		return [self.attack_descriptions[randint(0, len(self.attack_descriptions)-1)], self.damage]		# Return damage and a random attack description from your list.
		

class PlasmaRay(SpaceWeapon):
	equip_description = "You have equipped your plasma ray."
	attack_descriptions = ["You should define one or more attack descriptions as a list in your subclass.", "This is an example secondary attack description"]
	
	def __init__(self):
		self.name = 'Plasma Ray'
		self.description = 'A trigger activated gun that shoots plasma rays, liquifying the opponents insides.'
		self.droppedDescription = "A gun-like object is on the ground in front of you."
		self.damage = 10
	def __str__(self):
		return "Name: {} Description: {} Damage: {}".format(self.name, self.description, self.damage)
		
class Lightsaber(SpaceWeapon):
	equip_description = "You arm yourself with your lightsaber."
	attack_descriptions = ["You should define one or more attack descriptions as a list in your subclass.", "This is an example secondary attack description"]
	
	def __init__(self):
		self.name = 'Lightsaber'
		self.description = 'You know exactly what this is.'
		self.droppedDescription = "A lightsaber is on the ground in front of you."
		self.damage = 15
	def __str__(self):
		return "Name: {} Description: {} Damage: {}".format(self.name, self.description, self.damage)
		
class FreezerKey(Item):
	def __init__(self):
		self.name = 'Key to the freezer'
		self.description = "Keep this; you'll need it later."
		self.droppedDescription = "A cold key is on the ground in front of you."
		self.damage = 15
	def __str__(self):
		return "Name: {} Description: {} Damage: {}".format(self.name, self.description, self.damage)