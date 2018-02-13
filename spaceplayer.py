import spaceweapons

class SpacePlayer:
    def __init__(self):
        self.inventory =[spaceweapons.PlasmaRay(), spaceweapons.Lightsaber(), 'Gold(5)', 'Crusty Bread']
        self.x = 9
        self.y = 9
    def print_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            print('*' + str(item))
        best_weapon = self.most_powerful_weapon()
        print("Your best weapon : {}".format(best_weapon))
        
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
        self.move(dx=0,dy=-1)
        
    def move_back(self):
        self.move(dx=0,dy=1)
        
    def move_right(self):
        self.move(dx=1,dy=0)
       
    def move_left(self):
        self.move(dx=-1,dy=0)
        
    