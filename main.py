#Illia
import tkinter as tk
from tkinter import messagebox
import random


class Player:
    def __init__(self):
        self.hp = 100
        self.inventory = []

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def heal(self, amount):
        self.hp += amount
        if self.hp > 100:
            self.hp = 100


class RPGGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Python RPG Game")
        self.player = Player()

        self.label = tk.Label(root, text="Witamy w Python RPG Game!", font=("Arial", 14))
        self.label.pack(pady=10)

        self.info_label = tk.Label(root, text=self.get_player_status(), font=("Arial", 12))
        self.info_label.pack(pady=10)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.create_location_buttons()

    def get_player_status(self):
        return f"HP: {self.player.hp} | Ekwipunek: {', '.join(self.player.inventory) or 'Pusty'}"

    def create_location_buttons(self):
        for widget in self.button_frame.winfo_children():
            widget.destroy()

        self.label.config(text="Wybierz lokację do podróży:")

        locations = [("Zamek", self.castle), ("Las", self.forest), ("Wieś", self.village)]
        for name, command in locations:
            button = tk.Button(self.button_frame, text=name, command=command, font=("Arial", 12))
            button.pack(side="left", padx=10)

    def update_status(self):
        self.info_label.config(text=self.get_player_status())
        self.check_player_death()

    def check_player_death(self):
        if self.player.hp <= 0:
            messagebox.showinfo("Koniec gry", "Twój bohater zginął! Gra zakończona.")
            self.root.destroy()

    def show_description(self, description, callback):
        messagebox.showinfo("Opis", description)
        callback()

    def castle(self):
        description = (
            "Wchodzisz do ogromnego i mrocznego zamku. Jego korytarze są pełne echa kroków, a "
            "z oddali słychać złowrogie szepty. Tutaj można znaleźć zarówno skarby, jak i niebezpieczeństwa."
        )
        self.show_description(description, lambda: self.show_actions(
            "Jesteś w zamku. Co chcesz zrobić?",
            [("Walcz z wrogiem", self.fight_enemy),
             ("Poznaj zamek", self.explore_castle),
             ("Wracać", self.create_location_buttons)]
        ))

    def forest(self):
        description = (
            "Znajdujesz się w gęstym lesie. Promienie słońca ledwo przedzierają się przez liście, "
            "a dookoła słychać odgłosy dzikich zwierząt. To miejsce pełne zasobów i zagrożeń."
        )
        self.show_description(description, lambda: self.show_actions(
            "Jesteś w lesie. Co chcesz zrobić?",
            [("Walcz z wrogiem", self.fight_enemy),
             ("Zbieraj jagody", self.collect_berries),
             ("Wracać", self.create_location_buttons)]
        ))

    def village(self):
        description = (
            "Wchodzisz do spokojnej wsi. Mieszkańcy są przyjaźni i chętnie opowiadają nowinki. "
            "Tutaj można znaleźć przydatne przedmioty i poznać ciekawe plotki."
        )
        self.show_description(description, lambda: self.show_actions(
            "Jesteś we wsi. Co chcesz zrobić?",
            [("Porozmawiaj z wieśniakiem", self.talk_to_villager),
             ("Odwiedź sklep", self.visit_shop),
             ("Wracać", self.create_location_buttons)]
        ))

    def show_actions(self, text, actions):
        self.label.config(text=text)
        for widget in self.button_frame.winfo_children():
            widget.destroy()

        for name, command in actions:
            button = tk.Button(self.button_frame, text=name, command=command, font=("Arial", 12))
            button.pack(side="left", padx=10)

    def fight_enemy(self):
        damage = random.randint(5, 15)
        self.player.take_damage(damage)
        reward = random.choice(["Eliksir zdrowia", "Miecz"])
        self.player.inventory.append(reward)
        messagebox.showinfo("Bitwa", f"Walczyłeś z wrogiem! Straciłeś {damage} HP i zdobyłeś {reward}.")
        self.update_status()
        self.create_location_buttons()

    def explore_castle(self):
        messagebox.showinfo("Badanie", "Znalazłeś złoty klucz!")
        self.player.inventory.append("Złoty klucz")
        self.update_status()
        self.create_location_buttons()

    def collect_berries(self):
        self.player.heal(10)
        messagebox.showinfo("Zbieranie jagód", "Zjadłeś jagody i odnowiłeś 10 HP!")
        self.update_status()
        self.create_location_buttons()

    def talk_to_villager(self):
        messagebox.showinfo("Rozmawiać", "Mieszkaniec opowiedział Ci o tajemniczym miejscu w lesie.")
        self.create_location_buttons()

    def visit_shop(self):
        messagebox.showinfo("Sklep", "Kupiłeś miecz za 10 monet!")
        self.player.inventory.append("Miecz")
        self.update_status()
        self.create_location_buttons()


if __name__ == "__main__":
    root = tk.Tk()
    game = RPGGame(root)
    root.mainloop()
