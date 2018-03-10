import spaceitems
import items

class SpacePlayer:
	def __init__(self):
		self.inventory =[]
		self.weapon = None
		self.x = 10
		self.y = 10
		self.hp = 70
		self.max_hp = 70
		self.strength = 15
		
	def print_inventory(self):
		print("Inventory:")
		best_weapon = None
		equipped_weapon = False
		for item in self.inventory:
			inventory_text = '* ' + item.name.title()
			if(item == self.weapon and not equipped_weapon):
				inventory_text += ' (equipped)'
				equipped_weapon = True
			print(inventory_text)
			best_weapon = self.most_powerful_weapon()
		if(best_weapon):
			print("Your best weapon is your {}.".format(best_weapon))
		else:
			print("You are not carrying any weapons.")
	
	def most_powerful_weapon(self):
		max_damage = 0
		best_weapon = None
		for item in self.inventory:
			try:
				if item.damage > max_damage:
					best_weapon = item
					max_damage = item.damage
			except AttributeError:
				pass
		return best_weapon
		
	def move(self, dx, dy):
		self.x += dx
		self.y += dy

	def move_forward(self):
		self.move(dx=0, dy=-1)

	def move_back(self):
		self.move(dx=0, dy=1)

	def move_right(self):
		self.move(dx=1, dy=0)

	def move_left(self):
		self.move(dx=-1, dy=0)
		
	def update_inventory(self):
		has_weapon = False
		for item in self.inventory:
			if(item == self.weapon):
				has_weapon = True
		if not has_weapon:
			self.weapon = None	# Drop the equipped item if it is no longer in inventory.
			
	def heal(self, amount):
		self.hp += amount
		if(self.hp > self.max_hp):
			self.hp = self.max_hp
			return "Your health is fully restored."
		else:
			return "Your health was restored by %d HP." % amount
			
	def take_damage(self, amount):
		self.hp -= amount
		if(self.hp <= 0):
			self.hp = 0
			return "Your health is critical... everything is getting dark."
		else:
			return "You took %d damage." % amount
			
	def is_alive(self):
		if(self.hp <= 0):
			return False
		else:
			return True
			
	
	def handle_input(self, verb, noun1, noun2):
		if(verb == 'check'):
			if(noun1 == 'self' or noun1 == 'health' or noun1 == 'hp'):
				return [True, "Your health is currently %d / %d." % (self.hp, self.max_hp)]
			for item in self.inventory:
				if item.name.lower() == noun1:
					return [True, item.check_text()]
		elif(verb == 'consume'):
			for item in self.inventory:
				if item.name.lower() == noun1:
					if(isinstance(item, spaceitems.SpaceFood)):
						heal_text = item.eatenText
						heal_text += " " + self.heal(item.addedHP)
						self.inventory.pop(self.inventory.index(item))
						return [True, heal_text]
		elif(verb == 'drink'):
			for item in self.inventory:
				if item.name.lower() == noun1:
					if(isinstance(item, spaceitems.SpaceFood)):
						heal_text = item.eatenText
						heal_text += " " + self.heal(item.addedHP)
						self.inventory.pop(self.inventory.index(item))
						return [True, heal_text]
		elif(verb == 'use'):
			for item in self.inventory:
				if item.name.lower() == noun1:
					if(isinstance(item, spaceitems.Medicine)):
						heal_text = item.usedText
						heal_text += " " + self.heal(item.addedHP)
						self.inventory.pop(self.inventory.index(item))
						return [True, heal_text]
		elif(verb == 'equip'):
			for item in self.inventory:
				if item.name.lower() == noun1:
					if(isinstance(item, spaceitems.SpaceWeapon)):
						if(self.weapon != item):
							self.weapon = item
							return [True, item.equip_description]
						else:
							return [True, "You already have your %s equipped." % item.name]
		elif(verb == 'unequip'):
			for item in self.inventory:
				if item.name.lower() == noun1:
					if(isinstance(item, items.Weapon)):
						if(self.weapon == item):
							self.weapon = None
							return [True, "You have unequipped your %s." % item.name]
			return [True, "That does not appear to be equipped right now."]
		return [False, ""]