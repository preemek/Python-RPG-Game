import random
class player:

    def __init__(self):
        self.name = "odtwarzacz"
        self.hp = 100
        self.inventory = []
        self.fight_bonus = 1
    
    def fight(self):
        return random.randint(2, 6) + self.fight_bonus
    
    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0

    def HP(self, ile):
        self.hp += ile
        if self.hp > 100:
            self.hp = 100

    
    def używac_przedmoit(self, przedmoit):
        if przedmoit == "Mikstura zdrowia":
            self.hp = min(self.hp + 10, 100)
            self.inventory.remove(przedmoit)
