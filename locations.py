 #lokacje
import random

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exploration_events = []
        self.enemies = []

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def add_event(self, event):
        self.exploration_events.append(event)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def add_enemy(self, enemy_type):
        self.enemies.append(enemy_type)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def explore(self, player):
     if not self.exploration_events:
        return "You didn't find anything interesting."
     if self.name == "Castle" and random.random() < 0.2:
        hp_loss = 20
        player.take_damage(hp_loss)
        return f"You triggered a trap and lost {hp_loss} HP!"
     event = random.choice(self.exploration_events)
     if "You found a sword" in event:
        if player.can_add_to_inventory():
            player.damage += 5
            player.inventory.append("Sword")
        else:
            return "Your inventory is full!"
     elif "You found a magic stone" in event:
        if player.can_add_to_inventory():
            player.inventory.append("Magic stone")
        else:
            return "Your inventory is full!"
     elif "You found a health potion" in event:
        if player.can_add_to_inventory():
            player.inventory.append("Health potion")
        else:
            return "Your inventory is full!"
     elif "lost" in event:
        hp_loss = int(event.split("lost ")[1].split(" HP")[0])
        player.take_damage(hp_loss)
     return event