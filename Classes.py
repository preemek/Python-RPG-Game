#Wiktor
import random
import Player
import json
from tkinter import *

# mace={"name":"Mace", "dmg": 3, "type":"weapon"}   #weapon_name={"name":"<weapon_name>", "dmg":<number to add to dmg>, "type":"weapon"} 

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

class location:
    def __init__(self, name, list_of_enemies, list_of_loot, list_of_NPC):
        self.name=name
        self.list_of_enemies=list_of_enemies #enemies that may appear in battle in that location
        self.list_of_loot=list_of_loot #during exploration you can find loot (każdy item musi mieć swoją szansę na wylosowanie)
        self.list_of_NPC=list_of_NPC #NPC that you can talk to
    

    def fight (self,player: Player): #rozpocznij walkę z przeciwnikiem z listy
        selected_enemy = random.choice(self.list_of_enemies)
        initiate_fight(player,selected_enemy)

    def exploration (self,player: Player): #szansa na zdobycie złota, broni, mikstury, itp.
        selected_event = random.choices(["loot"],weights=[1]) #losowanie typu wydarzenia
        if selected_event == "loot":
            drop_chances= [item["drop_chance"] for item in self.list_of_loot]
            found_item = random.choices(self.list_of_loot,weights=drop_chances)
            player_found_an_item(player,found_item)

        else:
            initiate_event(player,selected_event)

    def talk (self,player: Player): #rozmawiaj z NPC / sklep?
        pass

def Game_Over (player: Player):
    #end of game 
    pass

def initiate_fight (player: Player,enemy):
    #napisz użytkownikowi z czym/kim walczy
    while enemy.hp > 0:
        
        pass



def player_found_an_item (player: Player, found_item):
    pass

def initiate_event (player: Player,event):
    pass

def interaction_with_NPC (player: Player,NPC):
    pass

"""
random.choices(mylist, weights = [10, 1, 1], k = 14)
weights - szansa na wylosowanie tej rzeczy
k - ile wartości jest zwróconych

do zrobienia funkcja do wyświetlania tekstu (taki print ale w tkinter)


"""