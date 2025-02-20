class Player:
    def __init__(self):
        self.name = "Hero"
        self.hp = 100
        self.level = 1
        self.experience = 0
        self.inventory = []
        self.base_damage = (5, 10)
        self.location = None

    def attack(self):
        import random
        return random.randint(*self.base_damage)

    def use_health_potion(self):
        if "Health Potion" in self.inventory:
            self.inventory.remove("Health Potion")
            self.hp += 20
            return True
        return False
