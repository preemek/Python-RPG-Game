import random

class Enemy:
    def __init__(self, name, hp, damage_range):
        self.name = name
        self.hp = hp
        self.damage_range = damage_range

    def attack(self):
        return random.randint(*self.damage_range)

enemies = [
    Enemy("Goblin", 30, (1, 8)),
    Enemy("Troll", 50, (5, 12)),
    Enemy("Bandit", 40, (3, 10))
]
