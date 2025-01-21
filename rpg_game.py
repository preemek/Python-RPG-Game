import tkinter 
import random
from player import Player
from enemy import Enemy
class RPGGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tekstowa Gra RPG")
        self.player = None
        self.enemy = None
        self.hp_label = tkinter.Label(self.root, text="HP: 100", font=("Helvetica", 14))
        self.hp_label.pack(pady=10)
        self.log_box = tkinter.Text(self.root, height=10, width=50)
        self.log_box.pack()
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tkinter.Label(self.root, text="Gra RPG", font=("Helvetica", 16))
        self.title_label.pack(pady=10)
        

        self.name_label = tkinter.Label(self.root, text="Wpisz swoje imię:")
        self.name_label.pack()

        self.name_entry = tkinter.Entry(self.root)
        self.name_entry.pack()

        self.start_button = tkinter.Button(self.root, text="Start", command=self.start_game)
        self.start_button.pack(pady=10)

        self.text_area = tkinter.Text(self.root, height=10, width=50, state=tkinter.DISABLED)
        
        self.explore_button = tkinter.Button(self.root, text="Eksploruj", command=self.explore)
        self.explore_button.pack(side=tkinter.LEFT, padx=5)

        self.fight_button = tkinter.Button(self.root, text="Walka", command=self.fight)
        self.fight_button.pack(side=tkinter.LEFT, padx=5)

        self.inventory_button = tkinter.Button(self.root, text="Ekwipunek", command=self.show_inventory)
        self.inventory_button.pack(side=tkinter.LEFT, padx=5)

        self.use_potion_button = tkinter.Button(self.root, text="Użyj mikstury", command=self.use_health_potion)
        self.use_potion_button.pack(side=tkinter.LEFT, padx=5)
        
    def start_game(self):
        player_name = self.name_entry.get()
        if player_name:
            self.player = Player(name=player_name, health=100)  
            self.update_hp_label() 
            self.log(f"Rozpoczęto grę! Witaj, {self.player.name} (HP: {self.player.health})")
        else:
            print("Podaj swoje imię, aby rozpocząć grę!")
    
    def update_hp_label(self):
        self.hp_label.config(text=f"HP: {self.player.health}")

    def enable_buttons(self):
        self.explore_button["state"] = tkinter.NORMAL
        self.fight_button["state"] = tkinter.NORMAL
        self.inventory_button["state"] = tkinter.NORMAL

    def enable_actions(self):
        self.explore_button["state"] = tkinter.NORMAL
        self.fight_button["state"] = tkinter.NORMAL
        self.inventory_button["state"] = tkinter.NORMAL

    def explore(self):
        locations = ["Las", "Zamek", "Wioska"]
        location = random.choice(locations)
        self.log(f"Udałeś się do {location}.")

        if location == "Las":
            self.enemy = Enemy("Wilk", random.randint(20, 50))
            self.log("Spotkałeś wroga! Czas na walkę!")
            self.fight_button["state"] = tkinter.NORMAL
            self.explore_button["state"] = tkinter.DISABLED
        elif location == "Zamek":
            item = "Mikstura zdrowia"
            self.player.inventory.append(item)
            self.log(f"Znalazłeś {item}")
            self.fight_button["state"] = tkinter.DISABLED
        elif location == "Wioska":
            self.player.add_exp(10)
            self.log("Spotkałeś kupca i zdobyłeś 10 EXP.")
            self.fight_button["state"] = tkinter.DISABLED
        self.text_area.see(tkinter.END)
    def use_health_potion(self):
    
        if "Mikstura zdrowia" in self.player.inventory:
           self.player.inventory.remove("Mikstura zdrowia")  
           heal_amount = random.randint(10, 30) 
           self.player.health += heal_amount
           if self.player.health > 100: 
              self.player.health = 100
           self.log(f"Użyłeś Mikstury zdrowia i przywróciłeś {heal_amount} HP.")
           self.update_hp_label()  
        else:
           self.log("Nie masz Mikstury zdrowia w ekwipunku!")

    def fight(self):
        if not self.enemy:
            self.log("Nie ma nikogo do walki.")
            return
        
        player_damage = random.randint(1, 10)
        enemy_damage = random.randint(1, 10)
        self.enemy.take_damage(player_damage)
        self.log(f"Zadałeś {player_damage} obrażeń {self.enemy.name}.")

        if self.enemy.health <= 0:
           self.log(f"Pokonałeś {self.enemy.name}!")
           self.enemy = None 
           self.fight_button["state"] = tkinter.DISABLED 
           self.explore_button["state"] = tkinter.NORMAL
           return
    
        self.log(f"{self.enemy.name} ma jeszcze {self.enemy.health} HP.")
        self.player.health -= enemy_damage
        if self.player.health < 0:
           self.player.health = 0 

        self.log(f"{self.enemy.name} zadał ci {enemy_damage} obrażeń.")

        self.update_hp_label()
        if self.player.health <= 0:
           self.log("Zginąłeś! Gra skończona.")
           


    def show_inventory(self):
        if not self.player.inventory:
            self.log("Twój ekwipunek jest pusty.")
        else:
            items = ", ".join(self.player.inventory)
            self.log(f"Twój ekwipunek: {items}")

    def log(self, message):
        self.text_area["state"] = tkinter.NORMAL
        self.text_area.insert(tkinter.END, message + "\n")
        self.text_area["state"] = tkinter.DISABLED
        self.text_area.see(tkinter.END)
        self.log_box.insert(tkinter.END, message + "\n")
        self.log_box.see(tkinter.END)












