import random
import time
from player import Player
from enemy import Enemy
from locations import Location

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class GameEngine:
    def __init__(self, root):  
        self.root = root 
        self.reset_game()
        self.stats_label = None
        self.in_battle = False
        self.current_enemy = None

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def reset_game(self):
     self.player = Player("Player")
     self.locations = {
        "forest": Location("Forest", "A dense, eerie forest with the sound of howling wolves."),
        "castle": Location("Castle", "An ancient castle filled with treasures and danger."),
        "village": Location("Village", "A cozy village with friendly villagers."),
     }
     self.current_location = self.locations["village"]
     self.logs = ""
     self.in_battle = False
     self.current_enemy = None


     self.enemy_types = {
        "wolf": {"name": "Wolf", "hp": 30, "damage": (2, 15), "exp": 10},
        "bandit": {"name": "Bandit", "hp": 120, "damage": (10, 45), "exp": 50},
        "dragon": {"name": "Dragon", "hp": 1000, "damage": (30, 80), "exp": 0},
    }

   
     self.locations["village"].add_event("You talked to an NPC and received a health potion!")
     self.locations["forest"].add_event("You found a sword!")
     self.locations["forest"].add_event("You fell into a trap, you lost 10 HP!")
     self.locations["castle"].add_event("You found a magic stone!")
     self.locations["castle"].add_event("You triggered a trap and lost 20 HP!") 

   
     for loc, enemies in {
        "forest": ["wolf"],
        "castle": ["bandit", "dragon"],
     }.items():
        for enemy in enemies:
            self.locations[loc].add_enemy(enemy)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def change_location(self, location_name):
        if location_name in self.locations:
            self.current_location = self.locations[location_name]

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def start_battle(self):
        if not self.current_location.enemies:
            self.logs += "No enemies to fight.\n"
            return
        enemy_type = random.choice(self.current_location.enemies)
        enemy_data = self.enemy_types[enemy_type]
        if enemy_type == "dragon" and self.player.level < 15:
            self.logs += "The dragon's power is overwhelming! You need to be at least level 15 to face it.\n"
            return
        self.current_enemy = Enemy(enemy_data["name"], enemy_data["hp"], enemy_data["damage"])
        self.logs += f"You encountered {self.current_enemy.name}!\n"
        self.in_battle = True

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def player_attack(self):
     if not self.in_battle:
        return
     if self.current_enemy.run_away(self.player.level):
        self.logs += f"The {self.current_enemy.name} ran away!\n"
        self.end_battle()
        return  
     base_damage = self.player.damage
     damage_range = (base_damage - 2, base_damage + 2) 
     player_damage = random.randint(*damage_range)
     if self.player.sword_active_turns > 0:
        player_damage *= 2 
        self.player.sword_active_turns -= 1 
        self.logs += f"You dealt {player_damage} damage with the sword's power! (Enemy HP: {max(self.current_enemy.hp, 0)})\n"
        if self.player.sword_active_turns == 0:
            self.logs += "The sword's power has faded.\n"
     else:
        self.logs += f"You dealt {player_damage} damage! (Enemy HP: {max(self.current_enemy.hp, 0)})\n"
     self.current_enemy.take_damage(player_damage)

     if self.current_enemy.is_defeated():
        self.logs += f"You defeated {self.current_enemy.name}!\n"
        self.player.gain_experience(self.enemy_types[self.current_enemy.name.lower()]["exp"])
        self.logs += f"You gained {self.enemy_types[self.current_enemy.name.lower()]['exp']} experience!\n"
        if self.player.experience >= self.player.level * 20:
            old_level = self.player.level
            self.player.level_up()
            self.logs += f"Congrats! You leveled up to level {self.player.level}!\n"
            self.logs += f"New Stats: HP: {self.player.max_hp}, Damage: {self.player.damage}\n"

        if self.current_enemy.name.lower() == "dragon":
            self.handle_victory() 
            return  
        self.end_battle()
        return
     self.enemy_turn()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def enemy_turn(self):
     if not self.in_battle:
        return

     enemy_damage = self.current_enemy.attack()
     self.player.take_damage(enemy_damage)
     self.logs += f"{self.current_enemy.name} dealt {enemy_damage} damage! (Your HP: {self.player.hp})\n"

     if self.player.magic_stone_active and self.player.magic_stone_turns > 0:
        heal_amount = int(self.player.max_hp * 0.25)
        self.player.heal(heal_amount)
        self.logs += f"The magic stone healed you for {heal_amount} HP (25% of max HP)!\n"
        self.player.magic_stone_turns -= 1

        if self.player.magic_stone_turns <= 0:
            self.player.magic_stone_active = False
            self.logs += "The magic stone's power has faded.\n"

     if self.player.hp <= 0:
        self.logs += "You lost!\n"
        self.handle_game_over()
        return
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def end_battle(self):
        self.in_battle = False
        self.current_enemy = None

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def talk_to_npc(self):
     if self.current_location.name.lower() == "village":
        self.logs += "You talk to a friendly villager. They give you a health potion!\n"
        if self.player.can_add_to_inventory():
            self.player.inventory.append("Health potion")
        else:
            self.logs += "Your inventory is full!\n"
     else:
        self.logs += "There's no one to talk to here.\n"
     self.update_stats()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def explore(self):
        if self.in_battle:
            self.logs += "You cannot explore during battle!\n"
            return
        event = self.current_location.explore(self.player)
        self.logs += event + "\n"
        self.update_stats()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def use_item(self, item_name):
     if item_name == "Health potion":
        self.player.heal(100)
        self.player.inventory.remove("Health potion")
        self.logs += "You drank a health potion and gained 20 HP!\n"
     elif item_name == "Sword":
        if "Sword" in self.player.inventory:
            self.player.sword_active_turns = 2 
            self.player.inventory.remove("Sword")  
            self.logs += "You activated the sword's power for 2 turns!\n"
        else:
            self.logs += "You don't have a sword in your inventory!\n"
     elif item_name == "Magic stone":
        if "Magic stone" in self.player.inventory:
            self.player.magic_stone_active = True
            self.player.magic_stone_turns = 4  
            self.player.inventory.remove("Magic stone") 
            self.logs += "You activated the magic stone's power! It will heal you after taking damage for 4 turns.\n"
        else:
            self.logs += "You don't have a magic stone in your inventory!\n"
     else:
        self.logs += "Invalid item selection.\n"
     self.update_stats()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def update_stats(self):
        if self.stats_label:
            self.stats_label.config(text=self.player.get_stats())

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def handle_game_over(self):
        self.logs += "Game Over! You have lost.\n"
        self.end_battle()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def handle_victory(self):
     self.logs += "Congratulations! You have defeated the dragon and saved the village! This is the end of your journey.\n"
     self.logs += "You finished the game. Thank you for playing!\n"
     self.update_stats() 
     self.end_game()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def end_game(self):
     self.logs += "Restarting the game in 10 seconds...\n"
     self.update_stats()  
     self.root.after(10000, self.reset_game)  