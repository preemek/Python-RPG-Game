import random

class Player:
    def __init__(self):
        self.name = "Gracz"
        self.hp = 100
        self.inventory = []
        self.attack_bonus = 0
    
    def attack(self):
        return random.randint(1, 10) + self.attack_bonus
    
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def heal(self, amount):
        self.hp += amount
        if self.hp > 100:
            self.hp = 100

    
    def use_item(self, item):
        if item == "Health potion":
            self.hp = min(self.hp + 20, 100)
            self.inventory.remove(item)

    
