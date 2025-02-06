import random

class Enemy:
    def __init__ (self,name :str, base_dmg :int, hp:int, XP_on_death:int):
        self.name=name
        self.base_dmg=base_dmg
        self.hp=hp
        self.XP_on_death=XP_on_death
    
    def attack(self):
        dmg_dealt = random.randint(self.base_dmg,int(self.base_dmg*1.5))
        return dmg_dealt
    def take_dmg (self, dmg_taken):
        self.hp -= dmg_taken


strong_ork = Enemy("Strong Ork",5,20,10)
ork = Enemy("Ork",2,10,4)
strong_wolf = Enemy("Strong Wolf",3,15,8)
wolf = Enemy("Wolf",1,6,2)
cursed_tree = Enemy("Cursed tree",2,20,8)