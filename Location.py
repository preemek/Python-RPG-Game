from Player import *
import Enemy
import random
import GameLogic


class location:
    def __init__(self, name, list_of_enemies, list_of_loot, list_of_NPC):
        self.name=name
        self.list_of_enemies=list_of_enemies #enemies that may appear in battle in that location
        self.list_of_loot=list_of_loot #during exploration you can find loot (każdy item musi mieć swoją szansę na wylosowanie)
        self.list_of_NPC=list_of_NPC #NPC that you can talk to
    

    def fight (self,player: Player): #rozpocznij walkę z przeciwnikiem z listy
        selected_enemy = random.choice(self.list_of_enemies)
        GameLogic.initiate_fight(player,selected_enemy)

    def exploration (self,player: Player): #szansa na zdobycie złota, broni, mikstury, itp.
        selected_event = random.choices(["loot"],weights=[1]) #losowanie typu wydarzenia
        if selected_event == "loot":
            drop_chances= [item["drop_chance"] for item in self.list_of_loot]
            found_item = random.choices(self.list_of_loot,weights=drop_chances)
            player.player_found_an_item(player,found_item)

        else:
            GameLogic.initiate_event(player,selected_event)

    def talk (self,player: Player): #rozmawiaj z NPC / sklep?
        appear_chances= [NPC["appear_chance"] for NPC in self.list_of_NPC]
        selected_NPC = random.choices(self.list_of_loot,weights=appear_chances)
        GameLogic.interaction_with_NPC(player,selected_NPC)