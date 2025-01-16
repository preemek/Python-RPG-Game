import tkinter as tk
from tkinter import messagebox
import random
from player import Player
from location import Forest, Castle, Village
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
        tk.Label(self.root, text="Enter your name to start the adventure!", font=("Arial", 16)).pack(pady=10)
        self.name_entry = tk.Entry(self.root, font=("Arial", 14))
        self.name_entry.pack(pady=10)

        self.start_button = tk.Button(self.root, text="Start Game", font=("Arial", 14), command=self.start_game)
        self.start_button.pack(pady=20)

        self.status_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.status_label.pack(pady=10)

    def update_status(self):
        self.status_label.config(text=f"{player.name}\nHP: {player.hp}\nLevel: {player.level}\nXP: {player.experience}\nLocation: {player.location.name if player.location else 'None'}\nInventory: {', '.join(player.inventory) if player.inventory else 'Empty'}")

    def start_game(self):
        player.name = self.name_entry.get()
        if not player.name:
            messagebox.showerror("Error", "Enter a name to start the game!")
            return
        self.main_menu()

    def main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text=f"Welcome {player.name}!", font=("Arial", 16)).pack(pady=10)

        locations = {
            "Forest": Forest(),
            "Castle": Castle(),
            "Village": Village()
        }

        for location in locations.values():
            tk.Button(self.root, text=location.name, font=("Arial", 14), command=lambda loc=location: self.enter_location(loc)).pack(pady=5)

        self.update_status()

    def enter_location(self, location):
        player.location = location
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text=f"{location.name}", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text=location.description, font=("Arial", 12)).pack(pady=10)

        for action in location.actions:
            tk.Button(self.root, text=action, font=("Arial", 14), command=lambda act=action: self.perform_action(location, act)).pack(pady=5)

        tk.Button(self.root, text="Back to Menu", font=("Arial", 14), command=self.main_menu).pack(pady=20)

    def perform_action(self, location, action):
        if action == "Fight":
            self.fight()
        elif action == "Explore":
            self.explore(location)
        elif action == "Talk":
            self.talk(location)

    def fight(self):
        enemy = random.choice(enemies)
        result = messagebox.askyesno("Fight", f"A wild {enemy.name} appears! Do you want to fight?")

        if result:
            while enemy.hp > 0 and player.hp > 0:
                enemy.hp -= player.attack()
                if enemy.hp <= 0:
                    player.experience += 20
                    if player.experience >= player.level * 50:
                        player.level += 1
                        player.base_damage = (player.base_damage[0] + 2, player.base_damage[1] + 2)
                    messagebox.showinfo("Victory", f"You defeated the {enemy.name}! Gained 20 XP.")
                    break

                player.hp -= enemy.attack()
                if player.hp <= 0:
                    messagebox.showerror("Game Over", "You have been defeated!")
                    self.root.destroy()
                    return

            self.update_status()

    def explore(self, location):
        event = random.choice(["found_item", "trap", "merchant"])
        if event == "found_item":
            item = random.choice(["Health Potion", "Sword"])
            player.inventory.append(item)
            messagebox.showinfo("Explore", f"You found a {item}!")
        elif event == "trap":
            damage = random.randint(5, 15)
            player.hp -= damage
            messagebox.showwarning("Trap", f"You triggered a trap and lost {damage} HP!")
            if player.hp <= 0:
                messagebox.showerror("Game Over", "You have been defeated by a trap!")
                self.root.destroy()
                return
        elif event == "merchant":
            messagebox.showinfo("Merchant", "You met a traveling merchant but had no gold to trade.")
        self.update_status()

    def talk(self, location):
        messagebox.showinfo("Talk", f"You talk to the locals in the {location.name}. They seem friendly but have little to say.")

# Uruchamianie gry
if __name__ == "__main__":
    initialize_player()
    root = tk.Tk()
    root.title("Text RPG Game")
    game = Game(root)
    root.mainloop()