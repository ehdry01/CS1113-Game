class EnemyGeneric():
    def __init__(self):
        raise NotImplementedError("Do not create raw Enemy objects.")
    def __str__(self):
        return self.name
class FFloopian(EnemyGeneric):
    def __init__(self):
        self.name = 'Floop Floopian'
        self.description = 'An Alien that acheives an amazing afterlife so long as they are killed by a great warrior.'
        self.strength = 5
        self.health = 15
class Gromflamite(EnemyGeneric):
    def __init__(self):
        self.name = 'Gromflamite'
        self.description = "An Insectoid Alien who's race runs the galactic government."
        self.strength = 10
        self.health = 20
class GreebyBobes(EnemyGeneric):
    def __init__(self):
        self.name = 'Greebybobe'
        self.description = "An Alien who's entire species was blown up on a reality show. This must be the last of its species"
        self.strength = 15
        self.health = 25
class GearPerson(EnemyGeneric):
    def __init__(self):
        self.name = 'Gear Person'
        self.description = "An Alien who's race of bio-mechanical aliens whose biology, technology, and society is built largely on gears"
        self.strength = 20
        self.health = 30