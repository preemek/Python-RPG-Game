#Wiktor
from tkinter import *
import random
import json


mace={"name":"Mace","dmg": 3,"Type":"weapon"}   #wszystkie przedmioty zdefiniowane wcześniej (Albo jako własna klasa) 

class Player:
    def __init__ (self,HP,Base_Dmg,name):
        self.name=name
        self.HP=10
        self.DEF=10
        self.XP=0
        self.Base_Dmg=2
        self.Equiped_Weapon=""
        self.Items={}   #{"item": <item here>, "quantity" : <quantity of item>}
        self.Location="" #?
    def take_dmg (self, dmg_taken): #jeżeli będą dodane zbroje, będzie to przydatne do obliczeń
        #dmg_taken = dmg_taken * max(1-self.DEF, 0.5) // ex. self.DEF = (0.2), armor negates 20% of dmg taken. If armor has negative value it will make player: Player take more dmg
        self.HP -= dmg_taken
        if self.HP <= 0:
            #Game Over
            pass
    def attack (self):
        dmg_dealt = random.randint(self.Base_Dmg,self.Base_Dmg*0.5) #losuj wartość na podstawie self.Base_Dmg
        dmg_dealt += self.Equiped_Weapon["dmg"]
        return dmg_dealt
    
    def use_item (self,used_item): 
        
        """example"""
        # if used_item == "my_item":
        #     do something
        # //if usable(ex. potions) decrese quantity!!!
        #items[used_item]["quantity"]-=1
        """-------"""

        #sprawdzenie czy wybrany przedmiot jest w ekwipunku???

        if used_item["Type"] == "weapon":
            self.Equiped_Weapon=used_item


class Enemy:
    def __init__ (self,name,base_dmg):
        self.name=name
        self.base_dmg=base_dmg
    
    def attack(self):
        dmg_dealt = random.randint(self.base_dmg,self.base_dmg*1.5)
        return dmg_dealt

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
        selected_event = random.choices(["loot"],weights=[1])
        if selected_event == "loot":
            found_item = random.choices([self.list_of_loot],weights=[self.list_of_loot["drop_chance"]])
            player_found_an_item(player,found_item)
        initiate_event(player,selected_event)

    def talk (self,player: Player): #rozmawiaj z NPC / sklep?
        pass

def Game_Over (player: Player):
    #end of game 
    pass

def initiate_fight (player: Player,enemy):
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