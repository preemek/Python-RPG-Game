 #przeciwniki
import random

class Enemy:
    def __init__(self, name, hp, damage_range):
        self.name = name
        self.hp = hp
        self.damage_range = damage_range

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def take_damage(self, amount):
        self.hp = max(self.hp - amount, 0)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def is_defeated(self):
        return self.hp <= 0

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def attack(self):
        return random.randint(self.damage_range[0], self.damage_range[1])

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def run_away(self, player_level):
     print(f"Checking if {self.name} runs away. Player level: {player_level}")   
     if self.name == "Wolf" and player_level >= 5:
        print(f"{self.name} is running away!")
        return True
     elif self.name == "Bandit" and player_level >= 15:
        print(f"{self.name} is running away!")
        return True
     return False