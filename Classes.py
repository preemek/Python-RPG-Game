#Wiktor
import random
import json


mace={"name":"Mace", "dmg": 3, "type":"weapon"}   #weapon_name={"name":"<weapon_name>", "dmg":<number to add to dmg>, "type":"weapon"} 

class Player:
    def __init__ (self,name :str,HP=10,Base_Dmg=2,Equiped_Weapon="",Items={},Lvl=0,XP=0,XP_needed_to_lvl_up=10):
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
    def use_item (self,used_item): 
        #example
        #if used_item == "my_item":
        #    do something
        #//if usable(ex. potions) decrese quantity!!!
        #items[used_item]["quantity"]-=1

        #sprawdzenie czy wybrany przedmiot jest w ekwipunku???

        if used_item["type"] == "weapon":
            self.Equiped_Weapon=used_item

def create_player (mode:str,file_number):
    """mode= <from_save_file> or <new_player>"""

    path=f"Python-RPG-Game\Player_Save_File{file_number}.json"
    if mode == "from_save_file":
        with open(path,'r') as player_save: 
            player_data = json.load(player_save)
            player = Player(player_data["name"],player_data["HP"],player_data["Base_Dmg"],player_data["Equiped_Weapon"],player_data["Items"],player_data["Lvl"],player_data["XP"],player_data["XP_needed_to_lvl_up"])
            player_save.close
        return player
    elif mode == "new_player":
        #zrób entry box dla imienia gracza, sprawdź czy nazwa nie jest za długa
        name="Bartek"
        player=Player(name)
        return player

def save_player_data(player:Player,file_number):
    path=f"Python-RPG-Game\Player_Save_File{file_number}.json"
    with open(path,'w') as save_file:
        json.dump(player.__dict__,save_file)
        save_file.close

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