class Player:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.inventory = []
        self.exp = 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def add_exp(self, exp_points):
        self.exp += exp_points
        print(f"{self.name} zdobył {exp_points} punktów doświadczenia. Teraz ma {self.exp} EXP.")

    def level_up(self):
        self.level += 1
        self.exp = 0
        self.health = 100

