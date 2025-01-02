import random



class Player:
    def __init__(self):
        self.name = ""
        self.hp = 100
        self.exp = 0
        self.level = 1
        self.inventory = []
    
    def attack(self):
        return random.randint(1, 10)
    
    def use_item(self, item):
        if item == "Health potion":
            self.hp = min(self.hp + 20, 100)
            self.inventory.remove(item)

class Enemy:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self):
        return random.randint(1, 10)



class Location:
    def __init__(self, name, description, enemies=None, items=None):
        self.name = name
        self.description = description
        self.enemies = enemies or []
        self.items = items or []

    def explore(self):
        if self.items:
            found_item = self.items.pop()
            return f'Znalazłeś {found_item}!', found_item
        else:
            return f'Nic nie znalazłeś', None

