import random


class Enemy:


    def __init__(self, nazwa, zdrowie, dmd_range):
        self.nazwa = nazwa
        self.zdrowie = zdrowie
        self.dmd_range = dmd_range

    def fight(self):
        return random.randint(*self.dmd_range)

enemies = [
    Enemy("Bałwan", 50, (2, 8)),
    Enemy("Mumia", 20, (3, 9)),
    Enemy("Błyszczka", 30, (2, 10))
]
