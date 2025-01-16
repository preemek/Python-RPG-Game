import random

class Enemy:
    def __init__ (self,name :str, base_dmg :int, hp:int, XP_on_death:int):
        self.name=name
        self.base_dmg=base_dmg
        self.hp=hp
        self.XP_on_death=XP_on_death
    
    def attack(self):
        dmg_dealt = random.randint(self.base_dmg,self.base_dmg*1.5)
        return dmg_dealt
    def take_dmg (self, dmg_taken):
        self.hp -= dmg_taken


#Może dodanie przeciwników jako klasy dziedziczące klasę Enemy żeby dodać unikatowe umiejętności
