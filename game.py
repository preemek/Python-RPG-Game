import tkinter 
import random

class RPGGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tekstowa Gra RPG")
        self.player_name = ""
        self.player_health = 100
        self.enemy_health = 0
        self.inventory = []
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
    def explore(self):
        locations = ["Las", "Wioska"]
        location = random.choice(locations)
        self.log(f"Udałeś się do {location}.")
        if location == "Las":
            self.enemy_health = 30
            self.log("Spotkałeś wroga! Czas na walkę!")
            self.fight_button["state"] = tkinter.NORMAL
        elif location == "Wioska":
            item = "Mikstura zdrowia"
            self.inventory.append(item)
            self.log(f"Znalazłeś {item}.")
    def fight(self):
        if self.enemy_health > 0:
            damage = random.randint(5, 15)
            self.enemy_health -= damage
            self.log(f"Zadałeś {damage} obrażeń wrogowi.")
            if self.enemy_health <= 0:
                self.log("Pokonałeś wroga!")
                self.fight_button["state"] = tkinter.DISABLED
            else:
                enemy_damage = random.randint(5, 10)
                self.player_health -= enemy_damage
                self.log(f"Wróg zadał ci {enemy_damage} obrażeń.")
                if self.player_health <= 0:
                    self.log("Przegrałeś. Koniec gry.")
                    self.disable_actions()
    def disable_actions(self):
        self.explore_button["state"] = tkinter.DISABLED
        self.fight_button["state"] = tkinter.DISABLED
    
    def log(self, message):
        self.text_area["state"] = tkinter.NORMAL
        self.text_area.insert(tkinter.END, message + "\n")
        self.text_area["state"] = tkinter.DISABLED
        self.text_area.see(tkinter.END)

if __name__ == "__main__":
    root = tkinter.Tk()
    game = RPGGame(root)
    root.mainloop()











