class Player:
    def __init__(self):
        self.hp = 100
        self.inventory = []
        self.max_hp = 100
        self.coins = 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def heal(self, amount):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def add_coins(self, amount):
        self.coins += amount