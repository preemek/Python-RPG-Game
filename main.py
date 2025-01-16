#Maks
import tkinter as tk
import random
from tkinter import messagebox

class RPG:
    def __init__(self, root):
        #tutaj gui
        self.root = root
        self.root.title("RpgPythonGame")
        self.root.geometry("800x600")
        

        #stats gracza
        self.player = {
            "Hp": 100,
            "Max_Hp": 100,
            "damage": 10,
            "inventory": []
        }

        
        #przeciwniki
        self.enemies = {
            "wolf": {"name": "Wolf", "Hp": 20, "damage": (5, 15)},
            "bandit": {"name": "Bandit", "Hp": 50, "damage": (10, 15)},
            "dragon": {"name": "Dragon", "Hp": 100, "damage": (15, 25)}
        }



        #lokacjee
        self.locations = {
            "forest":{
                "description": "You enter a dense, eerie forest, in a middle of a night. As you hear howling, you decide to take out your weapon. This is the start of your journey, may the moon be your guide",
                "actions": ["Explore the forest", "Fight a wolf", "Return to village"]
            }
            "castle":{
                "description": "You enter an ancient castle, while it looks empty, it doesn't feel like so",
                "actions": ["Explore the castle", "Fight a bandit", "Return to village"]
            }
            "village":{
                "description": "You are inside of a cozy village, whether to rest or visit merchant is up to you",
                "actions":  ["Buy a potion", "Rest and heal", "Go to the forest", "Go to the castle"]
            }
        }

        current_location = None

        #Aktualna lok i start gry.
        def start_game():
            global current_location
            current_location = "village"
            update_location()
         
        #Update statystyk i loc
        def update_location():
            location_label.config(text=f"Location: {current_location}")
            description_label.config(text=locations[current_location])
            update_stats()

        def update_stats():
            stats_label.config(
                text=f"HP: {player['Hp']}/{player['Max_Hp']}"
            )
       
        #Przycisk akcji
        actions_frame = tk.Frame(root)
        actions_frame.pack()

        fight_button = tk.Button(actions_frame, text="Fight", command=fight)
        fight_button.pack(side=tk.LEFT)

        explore_button = tk.Button(actions_frame, text="Exploration", command=explore)
        explore_button.pack(side=tk.LEFT)

        use_item_button = tk.Button(actions_frame, text="Use an item", command=use_item)
        use_item_button.pack(side=tk.LEFT)


        #tekst
        self.story_label = tk.Label(root, text="", wraplength=700, font=("Arial", 14), justify="center")
        self.story_label.pack(pady=20)

        #statystyka
        self.stats.label = tk.Label(root, text="")
        stats.label.pack()





    

        

