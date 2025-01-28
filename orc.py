from enemy import Enemy

class Orc(Enemy):
    def __init__(self):
        super().__init__("Orc", hp=90, min_attack=15, max_attack=25)