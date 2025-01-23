import json
import random
Mace={"name":"Mace", "dmg": 3, "type":"weapon","quantity":1}
health_potion ={"name":"health_potion","HP": 5}

class Player:
    def __init__ (self,name="None",HP=10,MaxHP=10,Base_Dmg=2,Equiped_Weapon="",Items={},Lvl=0,EXP=0,EXP_needed_to_lvl_up=10):
        self.name=name
        self.HP=HP
        self.MaxHP=MaxHP
        # self.DEF=10
        self.Lvl=Lvl
        self.EXP=EXP
        self.EXP_needed_to_lvl_up=EXP_needed_to_lvl_up
        self.Base_Dmg=Base_Dmg
        self.Equiped_Weapon=Equiped_Weapon
        self.Items=Items   # accesing items <name>.Items[f"{<accesed item>["name"]}"]["quantity"]
        # self.Location="" 
    def take_dmg (self, dmg_taken): #jeżeli będą dodane zbroje, będzie to przydatne do obliczeń
        #dmg_taken = dmg_taken * max(1-self.DEF, 0.5) // ex. self.DEF = (0.2), armor negates 20% of dmg taken. If armor has negative value it will make player: Player take more dmg
        self.HP -= dmg_taken
        if self.HP <= 0:
            #Game Over
            pass

    def attack (self):
        dmg_dealt = random.randint(self.Base_Dmg,self.Base_Dmg*1.5) #losuj wartość na podstawie self.Base_Dmg
        dmg_dealt += self.Equiped_Weapon["dmg"]
        return dmg_dealt
    
    def recieve_EXP (self,amount_of_EXP):
        self.EXP+=amount_of_EXP
        if self.EXP >= self.EXP_needed_to_lvl_up:
            self.EXP -= self.EXP_needed_to_lvl_up
            self.Lvl+=1
            self.EXP_needed_to_lvl_up *= 1.2
            int(self.EXP_needed_to_lvl_up)
            
    def player_found_an_item (self, found_item):
        if f"{found_item["name"]}" in self.Items:
            self.Items[found_item["name"]]["quantity"]+=1
        else:
            self.Items[f"{found_item["name"]}"]=found_item

        #{"item": <item here>, "quantity" : <quantity of item>}
# Mace={"name":"Mace", "dmg": 3, "type":"weapon"}   #weapon_name={"name":"<weapon_name>", "dmg":<number to add to dmg>, "type":"weapon"} 

    def use_item (self,used_item): 
        #example
        #if used_item == "my_item":
        #    do something
        #//if usable(ex. potions) decrese quantity!!!
        #items[used_item]["quantity"]-=1

        #sprawdzenie czy wybrany przedmiot jest w ekwipunku

        if used_item["type"] == "weapon":
            self.Equiped_Weapon=used_item
        
        if used_item["name"] == "health_potion":
            self.HP += min(used_item["hp"],self.MaxHP)


    def create_player (self,mode:str,file_number=0,*,input_name=""):
        """mode= <from_save_file> or <new_player>"""
            
        path=f"Python-RPG-Game/Player_Save_File{file_number}.json"
        if mode == "from_save_file":
            with open(path,'r') as player_save: 
                player_data = json.load(player_save)
                # zapisanie informacji o graczu
                self.name=player_data["name"]
                self.HP=player_data["HP"]
                self.MaxHP=player_data["MaxHP"]
                self.Lvl=player_data["Lvl"]
                self.EXP=player_data["EXP"]
                self.EXP_needed_to_lvl_up=player_data["EXP_needed_to_lvl_up"]
                self.Base_Dmg=player_data["Base_Dmg"]
                self.Equiped_Weapon=player_data["Equiped_Weapon"]
                self.Items=player_data["Items"]
                # ---
                player_save.close


        elif mode == "new_player":
            name=input_name
            self.name=name
            
    def save_player_data(self,file_number):
        path=f"Python-RPG-Game/Player_Save_File{file_number}.json"
        try:
            with open(path,'w') as save_file:
                json.dump(self.__dict__,save_file)
                save_file.close
        except Exception as err:
            print(err)
