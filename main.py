#Wiktor
from tkinter import *
import random
import json

class Player:
    HP=10
    Base_Dmg=2
    Dmg_with_weapon=Base_Dmg
    Gold=0
    Weapons=[]
    Equiped_Weapon=""
    items={}
    location=""

    def equip_weapon (Weapon):
        Player.Equiped_Weapon = Weapon
        Player.Dmg_with_weapon = Player.Base_Dmg + Weapon["dmg"]

class location:
    def __init__(self, name, list_of_enemies, list_of_weapons, list_of_NPC):
        self.name=name
        self.list_of_enemies=list_of_enemies #enemies that may appear in battle in that location
        self.list_of_weapons=list_of_weapons #during exploration you can find gold or weapon or nothing / or some special event
        self.list_of_NPC=list_of_NPC #NPC that you can talk to
    

    def fight (self): #rozpocznij walkę z przeciwnikiem z listy
        pass
    def exploration (self): #szansa na zdobycie złota
        pass
    def talk (self): #rozmawiaj z NPC / sklep?
        pass


mace={"name":"Mace","dmg": 3}

Player.Weapons.append(mace)

Player.equip_weapon(mace)

print(f" {Player.Equiped_Weapon["name"]}  {Player.Dmg_with_weapon} ")

