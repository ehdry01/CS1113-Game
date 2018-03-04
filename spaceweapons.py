class SpaceWeapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")
    def __str__(self):
        return self.name
class PlasmaRay(SpaceWeapon):
    def __init__(self):
        self.name = 'Plasma Ray'
        self.description = 'A trigger activated gun that shoots plasma rays, liquifying the opponents insides.'
        self.damage = 10
    def __str__(self):
        return "Name: {} Description: {} Damage: {}".format(self.name, self.description, self.damage)
class Lightsaber(SpaceWeapon):
    def __init__(self):
        self.name = 'Lightsaber'
        self.description = 'You know exactly what this is.'
        self.damage = 15
    def __str__(self):
        return "Name: {} Description: {} Damage: {}".format(self.name, self.description, self.damage)
