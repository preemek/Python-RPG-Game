from enemy import Enemy

class Goblin(Enemy):
    def __init__(self):
        super().__init__("Goblin", hp=70, min_attack=10, max_attack=15)