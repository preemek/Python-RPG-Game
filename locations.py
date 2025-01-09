import tkinter as tk
from tkinter import messagebox
import random

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description


    def explore(self, player):
        pass



class Village(Location):
    def __init__(self):
        super().__init__("Wioska", "Wioska pełna mieszkańców.")
        self.enemies = [Enemy("Złodziej", 20), Enemy("Rzezimieszek", 25)]

    def explore(self, player):
        messagebox.showinfo("Eksploracja", f"Eksplorujesz {self.name}. {self.description}")
        found_item = random.choice(["Mikstura zdrowia", "Jabłko", "Wiśnie" None])
        if found_item:
            messagebox.showinfo("Znalezisko", f"Znalazłeś: {found_item}!")
            player.inventory.append(found_item)

class Forest(Location):
    def __init__(self):
        super().__init__(
            name="Las", 
            description="Ciemny, tajemniczy las pełen niespodzianek", 
            enemies=["Gremlin", "Mroczny elf", "Zły wilk"], 
            items=["Sword", "Bow", "Herbs"])
        
     def explore(self, player):
        messagebox.showinfo("Eksploracja", f"Eksplorujesz {self.name}. {self.description}")
        found_item = random.choice(["Miecz", "Łuk", "Zioła" None])
        if found_item:
            messagebox.showinfo("Znalezisko", f"Znalazłeś: {found_item}!")
            player.inventory.append(found_item)   


class Castle(Location):
    def __init__(self):
        super().__init__(
            name="Zamek",
            description="Opuszczony zamek pełen basniowych potworów",
            enemies=["Black knight", "Medusa", "Cerber"]
            items=["Shield", "Gold", "Helmet"]

        )


