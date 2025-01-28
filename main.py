#Illia
import tkinter as tk
from tkinter import messagebox
import random


class Player:
    def __init__(self):
        self.hp = 100
        self.inventory = []
        self.max_hp = 100

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def heal(self, amount):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp


class Enemy:
    def __init__(self, name, hp, min_attack, max_attack):
        self.name = name
        self.hp = hp
        self.min_attack = min_attack
        self.max_attack = max_attack

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def get_attack_power(self):
        return random.randint(self.min_attack, self.max_attack)


class Goblin(Enemy):
    def __init__(self):
        super().__init__("Goblin", hp=70, min_attack=10, max_attack=15)


class Orc(Enemy):
    def __init__(self):
        super().__init__("Orc", hp=90, min_attack=15, max_attack=25)



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
        return f"HP: {self.player.hp}/{self.player.max_hp} | Inventory: {', '.join(self.player.inventory) or 'Empty'}"

    def create_location_buttons(self):
        for widget in self.button_frame.winfo_children():
            widget.destroy()

        self.label.config(text="Witamy w Python RPG Game!")

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
            self.root.quit()

    def castle(self):
        description = (
            "Wchodzisz do ogromnego i mrocznego zamku. Jego korytarze są pełne echa kroków, a "
            "z oddali słychać złowrogie szepty. Tutaj można znaleźć zarówno skarby, jak i niebezpieczeństwa."
        )
        self.show_description(description, self.create_castle_actions)

    def forest(self):
        description = (
            "Znajdujesz się w gęstym lesie. Promienie słońca ledwo przedzierają się przez liście, "
            "a dookoła słychać odgłosy dzikich zwierząt. To miejsce pełne zasobów i zagrożeń."
        )
        self.show_description(description, self.create_forest_actions)

    def village(self):
        description = (
            "Wchodzisz do spokojnej wsi. Mieszkańcy są przyjaźni i chętnie opowiadają nowinki. "
            "Tutaj można znaleźć przydatne przedmioty i poznać ciekawe plotki."
        )
        self.show_description(description, self.create_village_actions)

    def show_description(self, description, callback):
        messagebox.showinfo("Opis", description)
        callback()

    def create_castle_actions(self):
        self.create_buttons(
            "Jesteś w zamku. Co chcesz zrobić?",
            [("Walcz z wrogiem", self.start_battle),
             ("Poznaj zamek", self.explore_castle),
             ("Wracać", self.create_location_buttons)]
        )

    def create_forest_actions(self):
        self.create_buttons(
            "Jesteś w lesie. Co chcesz zrobić?",
            [("Walcz z wrogiem", self.start_battle),
             ("Zbieraj jagody", self.collect_berries),
             ("Wracać", self.create_location_buttons)]
        )

    def create_village_actions(self):
        self.create_buttons(
            "Jesteś we wsi. Co chcesz zrobić?",
            [("Porozmawiaj z wieśniakiem", self.talk_to_villager),
             ("Odwiedź sklep", self.visit_shop),
             ("Wracać", self.create_location_buttons)]
        )

    def create_buttons(self, text, actions):
        self.label.config(text=text)
        for widget in self.button_frame.winfo_children():
            widget.destroy()

        for name, command in actions:
            button = tk.Button(self.button_frame, text=name, command=command, font=("Arial", 12))
            button.pack(side="left", padx=10)

    def start_battle(self):
        self.enemy = random.choice([Goblin(), Orc()])
        self.show_battle_menu()

    def show_battle_menu(self):
        self.label.config(text=f"Walczysz z {self.enemy.name}! HP {self.enemy.name}: {self.enemy.hp}")
        for widget in self.button_frame.winfo_children():
            widget.destroy()

        actions = [
            ("Atakuj", self.attack_enemy),
            ("Lecz się", self.heal_player)
        ]
        for name, command in actions:
            button = tk.Button(self.button_frame, text=name, command=command, font=("Arial", 12))
            button.pack(side="left", padx=10)

    def attack_enemy(self):
        if "Miecz" in self.player.inventory:
            player_damage = random.randint(15, 25)
        else:
            player_damage = random.randint(10, 15)
        
        self.enemy.take_damage(player_damage)

        if self.enemy.hp <= 0:
            messagebox.showinfo("Bitwa wygrana", f"Pokonałeś {self.enemy.name}!")
            reward = random.choice(["Złoty klucz", "Miecz", "Eliksir zdrowia"])
            self.player.inventory.append(reward)
            self.update_status()
            self.create_location_buttons()
            return

        enemy_damage = self.enemy.get_attack_power()
        self.player.take_damage(enemy_damage)
        messagebox.showinfo("Atak", f"Zadałeś {player_damage} obrażeń. {self.enemy.name} zadał {enemy_damage} obrażeń!")
        self.update_status()

        if self.player.hp > 0:
            self.show_battle_menu()

    def heal_player(self):
        if "Eliksir zdrowia" in self.player.inventory:
            self.player.inventory.remove("Eliksir zdrowia")
            self.player.heal(20)
            messagebox.showinfo("Leczenie", "Użyłeś eliksiru zdrowia i odzyskałeś 20 HP!")
        else:
            messagebox.showinfo("Brak eliksiru", "Nie masz eliksirów zdrowia!")
        self.update_status()
        self.show_battle_menu()

    def explore_castle(self):
        found_thing = random.choice(["Złoty klucz", "Eliksir zdrowia"])
        messagebox.showinfo("Badanie", f"Znalazłeś {found_thing}!")
        self.player.inventory.append(found_thing)
        self.update_status()
        self.create_castle_actions()

    def collect_berries(self):
        self.player.heal(10)
        messagebox.showinfo("Zbieranie jagód", "Zjadłeś jagody i odnowiłeś 10 HP!")
        self.update_status()
        self.create_forest_actions()

    def talk_to_villager(self):
        messagebox.showinfo("Rozmowa", "Mieszkaniec opowiedział Ci o tajemniczym miejscu w lesie.")
        self.create_village_actions()

    def visit_shop(self):
        if "Miecz" not in self.player.inventory:
            messagebox.showinfo("Sklep", "Kupiłeś miecz!")
            self.player.inventory.append("Miecz")
        else:
            messagebox.showinfo("Sklep", "Już masz miecz!")
        self.update_status()
        self.create_village_actions()


if __name__ == "__main__":
    root = tk.Tk()
    game = RPGGame(root)
    root.mainloop()
