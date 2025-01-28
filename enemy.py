import random

class Enemy:
    def __init__(self, name, hp, min_attack, max_attack):
        self.name = name
        self.hp = hp
        self.min_attack = min_attack
        self.max_attack = max_attack

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def get_attack_power(self):
        return random.randint(self.min_attack, self.max_attack)