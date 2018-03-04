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

class PlasmaRay(Item):
    def __init__(self):
        self.name = 'Plasma Ray'
        self.description = 'A trigger activated gun that shoots plasma rays, liquifying the opponents insides.'
        self.droppedDescription = "A gun-like object is on the ground in front of you."
        self.damage = 10
    def __str__(self):
        return "Name: {} Description: {} Damage: {}".format(self.name, self.description, self.damage)
class Lightsaber(Item):
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