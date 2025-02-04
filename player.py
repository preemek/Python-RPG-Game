# gracz
class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.max_hp = 100
        self.damage = 500
        self.inventory = []
        self.max_inventory_size = 5
        self.experience = 0
        self.level = 1
        self.magic_stone_active = False  
        self.magic_stone_turns = 0     
        self.sword_active_turns = 0     

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0  

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def heal(self, amount):
        if self.hp > 0:
            self.hp = min(self.hp + amount, self.max_hp)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def gain_experience(self, xp):
        self.experience += xp
        if self.experience >= self.level * 20:
            self.level_up()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def level_up(self):
     old_level = self.level
     self.level += 1
     self.max_hp += 10
     self.damage += 2
     print(f"Player leveled up from {old_level} to {self.level}!")  

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def get_stats(self):
        """Return a formatted string of the player's stats."""
        return f"HP: {self.hp}/{self.max_hp} | Level: {self.level} | EXP: {self.experience}/{self.level * 20}"

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def can_add_to_inventory(self):
        """Check if the inventory has space for new items."""
        return len(self.inventory) < self.max_inventory_size