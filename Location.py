from Enemy import ork, strong_ork, wolf, strong_wolf, cursed_tree
from Enemy import Enemy
import random

class location:
    def __init__(self, name, list_of_enemies, list_of_loot, list_of_NPC,list_of_events):
        self.name=name
        self.list_of_enemies=list_of_enemies #enemies that may appear in battle in that location
        self.list_of_loot=list_of_loot #during exploration you can find loot (każdy item musi mieć swoją szansę na wylosowanie)
        self.list_of_NPC=list_of_NPC #NPC that you can talk to
        self.list_of_events=list_of_events

    def fight (self) -> Enemy: #wybierz przeciwnika z listy
        """returns Enemy class"""
        selected_enemy = random.choice(self.list_of_enemies)
        return selected_enemy
    
    def exploration (self) -> str:  #szansa na zdobycie złota, broni, mikstury, itp.
        """returns name of event"""
        drop_chances = [event["find_chance"] for event in self.list_of_events]
        selected_event = random.choices(self.list_of_events,weights=drop_chances) #losowanie typu wydarzenia
        return selected_event[0]["name"]

    def draw_random_item (self) -> dict:
        """returns item -> dict"""
        drop_chances = [item["drop_chance"] for item in self.list_of_loot]
        found_item = random.choices(self.list_of_loot,weights=drop_chances)
        found_item=found_item[0]

        if found_item["type"]=="gold":
            found_item["amount"]=random.randint(found_item["min_amount"],found_item["max_amount"])
        
        return found_item
    
    def talk (self) ->list:
        """returns list of npc avaiable"""
        return self.list_of_NPC
    
    @staticmethod
    def draw_from_wishing_well() -> dict|str:
        items=[
            {"type":"potion", "name":"Huge health potion","hp": 20,"drop_chance":3},
            {"type":"weapon", "name":"Rusty Sword", "dmg": 10, "drop_chance":1},
            {"type":"junk","name":"Junk","drop_chance":5}
        ]

        if random.choices([True,False],weights=[1,9])[0]:
            drop_chances = [item["drop_chance"] for item in items]
            found_item = random.choices(items,weights=drop_chances)
            return found_item[0]
        else:
            return "nothing"
    

wooden_sword = {"type":"weapon","name":"Woooden sword","dmg":1,"drop_chance":5}
mace = {"type":"weapon", "name":"Mace", "dmg": 3, "drop_chance":2}
gold_forest = {"type":"gold","name":"gold","min_amount":5,"max_amount":10,"drop_chance":7}
gold_village = {"type":"gold","name":"gold","min_amount":2,"max_amount":5,"drop_chance":7}
gold_castle = {"type":"gold","name":"gold","min_amount":10,"max_amount":15,"drop_chance":7}
small_health_potion ={"type":"potion", "name":"Small health potion","hp": 5,"drop_chance":5}
big_health_potion ={"type":"potion", "name":"Big health potion","hp": 10,"drop_chance":5}

loot={"name":"loot","find_chance":1}
wishing_well={"name":"wishing well","find_chance":3}

Travel_Person ={"name":" Travel Person","dialog":"Hello adventuer, do you want to have a ride?\nWhere do you want to go?"}
Bob = {"name":"Bob","dialog":"Hello adventuer, have you heard of princess trapped in the castle?\nBut its very scary there so prepare yourself before you go there\n"}

forest = location("forest",[ork,wolf,cursed_tree],[gold_forest,small_health_potion,mace],[Travel_Person],[loot,wishing_well])
village = location("village",["no enemies"],[gold_village,wooden_sword],[Travel_Person,Bob],[loot,wishing_well])
castle = location("castle",[strong_ork,strong_wolf],[gold_castle],[Travel_Person],[loot])