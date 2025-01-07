import tkinter 
import random
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.exp = 0
        self.level = 1
        self.inventory = []
    def level_up(self):
        if self.exp >= 100:
            self.level += 1
            self.exp -= 100
            self.health = 100
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

class RPGGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tekstowa Gra RPG")
        player_name = input("Podaj swoje imię!")
        self.player = Player(player_name)
        self.enemy = None
        self.create_widgets()

    def create_widgets(self):
        self.label = tkinter.Label(self.root, text="Witamy w grze RPG!", font=("Helvetica", 16))
        self.label.pack(pady=10)
        self.entry = tkinter.Entry(self.root)
        self.entry.pack()
        self.start_button = tkinter.Button(self.root, text="Rozpocznij", command=self.start_game)
        self.start_button.pack(pady=10)
        self.text_area = tkinter.Text(self.root, height=10, width=40, state=tkinter.DISABLED)
        self.text_area.pack(pady=10)

        self.explore_button = tkinter.Button(self.root, text="Eksploruj", command=self.explore, state=tkinter.DISABLED)
        self.explore_button.pack(side=tkinter.LEFT, padx=5)
        self.fight_button = tkinter.Button(self.root, text="Walka", command=self.fight, state=tkinter.DISABLED)
        self.fight_button.pack(side=tkinter.LEFT, padx=5)
        self.inventory_button = tkinter.Button(self.root, text="Ekwipunek", command=self.show_inventory, state=tkinter.DISABLED)
        self.inventory_button.pack(side=tkinter.LEFT, padx=5)
    def start_game(self):
        self.player_name = self.entry.get()
        if self.player_name:
            self.log(f"Czesc, {self.player_name}! Witamy w grze.")
            self.entry.pack_forget()
            self.start_button.pack_forget()
            self.enable_actions()
        else:
            self.log("Podaj swoje imię!")
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
        elif location == "Zamek":
            item = "Mikstura zdrowia"
            self.player.inventory.append(item)
            self.log(f"Znalazłeś {item}")
        elif location == "Wioska":
            self.player.add_exp(10)
            self.log("Spotkałeś kupca i zdobyłeś 10 EXP.")
    def fight(self):
        if not self.enemy:
            self.log("Nie ma nikogo do walki.")
            return
        player_damage = random.randint(1, 10)
        self.enemy.take_damage(player_damage)
        self.log(f"Zadałeś {player_damage} obrażeń {self.enemy.name}.")
        if self.enemy.health <= 0:
            self.log(f"Pokonałeś {self.enemy.name}!")
            self.enemy = None
            return
        enemy_damage = random.randint(1, 10)
        self.player.take_damage(enemy_damage)
        self.log(f"{self.enemy.name} zadał ci {enemy_damage} obrażeń.")
        if self.player.health <= 0:
            self.log("Zostałeś pokonany. Koniec gry.")
            self.disable_buttons()

    def show_inventory(self):
        if not self.player.inventory:
            self.log("Twój ekwipunek jest pusty.")
        else:
            items = ", ".join(self.player.inventory)
            self.log(f"Twój ekwipunek: {items}")

    def disable_actions(self):
        self.explore_button["state"] = tkinter.DISABLED
        self.fight_button["state"] = tkinter.DISABLED
        self.inventory_button["state"] = tkinter.DISABLED
    
    def log(self, message):
        self.text_area["state"] = tkinter.NORMAL
        self.text_area.insert(tkinter.END, message + "\n")
        self.text_area["state"] = tkinter.DISABLED
        self.text_area.see(tkinter.END)

if __name__ == "__main__":
    root = tkinter.Tk()
    game = RPGGame(root)
    root.mainloop()










