import json
import random

class Player:
    def __init__ (self,name="",HP=10,Base_Dmg=2,Equiped_Weapon="",Items={},Lvl=0,XP=0,XP_needed_to_lvl_up=10):
        self.name=name
        self.HP=HP
        # self.DEF=10
        self.Lvl=Lvl
        self.XP=XP
        self.XP_needed_to_lvl_up=XP_needed_to_lvl_up
        self.Base_Dmg=Base_Dmg
        self.Equiped_Weapon=Equiped_Weapon
        self.Items=Items   #{"item": <item here>, "quantity" : <quantity of item>}
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
    
    def recieve_XP (self,amount_of_XP):
        self.XP+=amount_of_XP
        if self.XP >= self.XP_needed_to_lvl_up:
            self.XP -= self.XP_needed_to_lvl_up
            self.Lvl+=1
            self.XP_needed_to_lvl_up *= 1.2
            int(self.XP_needed_to_lvl_up)
            
    def player_found_an_item (self, found_item):
        pass

    def Open_inventory():
        #toplevel widget
        pass
# mace={"name":"Mace", "dmg": 3, "type":"weapon"}   #weapon_name={"name":"<weapon_name>", "dmg":<number to add to dmg>, "type":"weapon"} 

    def use_item (self,used_item): 
        #example
        #if used_item == "my_item":
        #    do something
        #//if usable(ex. potions) decrese quantity!!!
        #items[used_item]["quantity"]-=1

        #sprawdzenie czy wybrany przedmiot jest w ekwipunku

        if used_item["type"] == "weapon":
            self.Equiped_Weapon=used_item


    def create_player (self,mode:str,file_number):
        """mode= <from_save_file> or <new_player>"""
            
        path=f"Player_Save_File{file_number}.json"
        if mode == "from_save_file":
            try:
                with open(path,'r') as player_save: 
                    player_data = json.load(player_save)
                    # zapisanie informacji o graczu
                    self.name=player_data["name"]
                    self.HP=player_data["HP"]
                    self.Lvl=player_data["Lvl"]
                    self.XP=player_data["XP"]
                    self.XP_needed_to_lvl_up=player_data["XP_needed_to_lvl_up"]
                    self.Base_Dmg=player_data["Base_Dmg"]
                    self.Equiped_Weapon=player_data["Equiped_Weapon"]
                    self.Items=player_data["Items"]
                    # ---
                    player_save.close
            except FileNotFoundError:
                print("File doesn't exist")
            except Exception as err:
                print(err)

        elif mode == "new_player":
            name=""
            if len(name) <= 15:
                self.name=name
            
    def save_player_data(self,file_number):
        path=f"Player_Save_File{file_number}.json"
        try:
            with open(path,'w') as save_file:
                json.dump(self.__dict__,save_file)
                save_file.close
        except Exception as err:
            print(err)
