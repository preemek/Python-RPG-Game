import random

class Enemy:
    def __init__(self, name, hp, damage_range):
        self.name = name
        self.hp = hp
        self.damage_range = damage_range

    def attack(self):
        return random.randint(*self.damage_range)

enemies = [
    Enemy("Bałwan", 50, (2, 8)),
    Enemy("Mumia", 20, (3, 9)),
    Enemy("Błyszczka", 30, (2, 10))
]