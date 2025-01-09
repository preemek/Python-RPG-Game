class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.exp = 0
        self.level = 1
        self.inventory = []
        
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def add_exp(self, exp_points):
        self.exp += exp_points
        if self.exp >= 20:
            self.level_up()

    def level_up(self):
        if self.exp >= 100:
            self.level += 1
            self.exp -= 100
            self.health = 100
