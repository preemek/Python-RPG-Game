import tkinter as tk
from tkinter import messagebox
import random



class RPGGame:
    def __init__(self):
        self.player = Player()

        self.locations = {
            "Wioska": Village(),
            "Las": Forest(),
            "Zamek": Castle()
        }

        self.current_location = self.locations["Wioska"]

        def explore(self):
            found_item = self.current_location.explore()

            if found_item:
                self.player.inventory.append(found_item)

        def fight(self):
            if not self.current_location.enemies:
                print("Walka", "Brak przeciwników w tej lokacji.")
                return
            
            enemy_name = random.choice(self.current_location.enemies)
            enemy = Enemy(enemy_name, 30)