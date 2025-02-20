import tkinter as tk
from tkinter import messagebox
import random
from player import Player
from location import basement,house,city  
from enemy import enemies

# Inicjalizacja gracza
def initialize_player():
    global player
    player = Player()

# Klasa gry
class Game:
    def __init__(self, root):
        self.root = root
        self.status_label = None
        self.name_entry = None
        self.start_button = None
        self.setup_start_screen()

    def setup_start_screen(self):
        tk.Label(self.root, text="Enter your name to start the adventure!", font=("Groow", 16)).pack(pady=10)
        self.name_entry = tk.Entry(self.root, font=("Groow", 14))
        self.name_entry.pack(pady=10)

        self.start_button = tk.Button(self.root, text="Start Game", font=("Groow", 14), command=self.start_game)
        self.start_button.pack(pady=20)

        self.status_label = tk.Label(self.root, text="", font=("Groow", 12))
        self.status_label.pack(pady=10)

    def update_status(self):
         self.status_label.config(text=f"{player.name}\nHP: {player.hp}\nLevel: {player.level}\nXP: {player.experience}\nLocation: {player.location.name if player.location else 'None'}\nInventory: {', '.join(player.inventory) if player.inventory else 'Empty'}")
    def start_game(self):
        player.name = self.name_entry.get()
        if not player.name:
            messagebox.showerror("Błąd", "Wprowadź nazwę, aby rozpocząć grę!")
            return
        self.main_menu()

    def main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text=f"Powitanie {player.name}!", font=("Groow", 20)).pack(pady=10)


        locations = {
            "basement":basement(),
            "house": house(),
            "city":city ()
        }

        for location in locations.values():
            tk.Button(self.root, text=location.name, font=("Groow", 18), command=lambda loc=location: self.enter_location(loc)).pack(pady=7)


        self.status_label = tk.Label(self.root, text = "", font=("Groow", 12))
        self.status_label.pack(pady=10)

        self.update_status()

    def enter_location(self, location):
        player.location = location
        for widget in self.root.winfo_children():
            widget.destroy()


        tk.Label(self.root, text=f"{location.name}", font=("Groow", 18)).pack(pady=10)
        tk.Label(self.root, text=location.description, font=("Groow", 14)).pack(pady=10)


        for action in location.actions:
            tk.Button(self.root, text=action, font=("Groow", 14), command=lambda act=action: self.perform_action(location, act)).pack(pady=5)

        tk.Button(self.root, text="Powrót do menu", font=("Groow", 14), command=self.main_menu).pack(pady=20)

    def perform_action(self, location, action):
        if action == "Fight":
            self.fight()
        elif action == "Explore":
            self.explore(location)
        elif action == "Talk":
            self.talk(location)

    def fight(self):
        enemy = random.choice(enemy)
        result = messagebox.askyesno("Walka", f"Dziki {enemy.name} pojawia się! Czy chcesz walczyć?")


        if result:
            while enemy.hp > 0 and player.hp > 0:
                enemy.hp -= player.attack()
                if enemy.hp <= 0:
                    player.experience += 20
                    if player.experience >= player.level * 50:
                        player.level += 1
                        player.base_damage = (player.base_damage[0] + 2, player.base_damage[1] + 2)
                    messagebox.showinfo("Zwycięzcay", f"Pokonałeś {enemy.name}! Zdobyte 35 XP.")
                    break

                player.hp -= enemy.attack()
                if player.hp <= 0:
                    messagebox.showerror("Koniec gry", "Zostałeś pokonany!")
                    self.root.destroy()
                    return

            self.update_status()

    def explore(self, location):
        event = random.choice(["znaleziony przedmiot", "pułapka", "kupiec"])
        if event == "znaleziony przedmiot":
            item = random.choice(["Mikstura Zdrowia", "Miecz"])
            player.inventory.append(item)
            messagebox.showinfo("Explore", f"Znalazłeś {item}!")
        elif event == "pułapka":
            damage = random.randint(5, 15)
            player.hp -= damage
            messagebox.showwarning("pułapka", f"Uruchomiłeś pułapkę i przegrałeś {dmg} HP!")
            if player.hp <= 0:
                messagebox.showerror("Koniec gry", "Zostałeś pokonany przez pułapkę!")
                self.root.destroy()
                return
        elif event == "kupiec":
            messagebox.showinfo("kupiec", "Spotkałeś podróżującego kupca, ale nie miałeś złota na handel.")

        self.status_label = tk.Label(self.root, text = "", font=("Groow", 14))
        self.status_label.pack(pady=10)
        
        self.update_status()

    def talk(self, location):
        messagebox.showinfo("Talk", f"Rozmawiasz z mieszkańcami w {location.name}. Wydają się przyjaźni, ale mają niewiele do powiedzenia.")

# Uruchamianie gry
if __name__ == "__main__":
    initialize_player()
    root = tk.Tk()
    root.title("Text RPG Game")
    game = Game(root)
    root.mainloop()