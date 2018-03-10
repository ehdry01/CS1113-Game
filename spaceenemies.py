import spaceitems

class EnemyGeneric():
    agro = False
    def __init__(self):
        raise NotImplementedError("Do not create raw Enemy objects.")
        if(len(self.loot) > 0):
            for item in loot:
                self.loot.append(item)
            else:
                self.loot = loot
    def __str__(self):
        return self.name
    def check_text(self):
        text = ""
       # if(self.direction):
           # text = "A %s is blocking your progress to the %s." % (self.name, self.direction)
        text += " " + self.name + " has attacked!"
        return text
    
    def take_damage(self, amount):
        self.hp -= amount
        if(self.hp <= 0):
            self.hp = 0
            defeat_text = "The %s is defeated." % self.name
            if(len(self.loot) > 0):
                defeat_text += " It dropped the following items: "
                for item in self.loot:
                    defeat_text += "* " + str(item)
            return defeat_text
        else:
            return "The %s took %d damage." % (self.name, amount)
			
    def is_alive(self):
        return self.hp > 0
    
    
class FFloopian(EnemyGeneric):
    def __init__(self):
        self.name = 'Floop Floopian'
        self.description = 'An Alien that acheives an amazing afterlife so long as they are killed by a great warrior.'
        self.damage = 1
        self.hp = 1
        self.agro = True
        self.loot = []
class Gromflamite(EnemyGeneric):
    def __init__(self):
        self.name = 'Gromflamite'
        self.description = "An Insectoid Alien who's race runs the galactic government."
        self.damage = 3
        self.hp = 2
        self.loot= []
        self.agro = True
class GreebyBobes(EnemyGeneric):
    def __init__(self):
        self.name = 'Greebybobe'
        self.description = "An Alien who's entire species was blown up on a reality show. This must be the last of its species"
        self.damage = 5
        self.hp = 5
        self.agro = True
        self.loot = []
class GearPerson(EnemyGeneric):
    def __init__(self):
        self.name = 'Gear Person'
        self.description = "An race of bio-mechanical aliens whose biology, technology, and society is built largely on gears"
        self.damage = 7
        self.hp = 10
        self.loot = [spaceitems.FreezerKey()]
        self.agro = True
class TelepathicSpider(EnemyGeneric):
    def __init__(self):
        self.name = 'Giant Telepathic spider'
        self.description = "From the dimension that formally had the best ice cream in the multi-verse"
        self.damage = 9
        self.hp = 15
        self.agro = True
        self.loot = []
class Gazorpian(EnemyGeneric):
    def __init__(self):
        self.name = 'Gazorpian'
        self.description = "One of the most violent species in the galaxy"
        self.damage = 12
        self.hp = 15
        self.agro = True
        self.loot = []