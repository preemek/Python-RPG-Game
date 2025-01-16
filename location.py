class Location:
    def __init__(self, name, description, actions):
        self.name = name
        self.description = description
        self.actions = actions

class Forest(Location):
    def __init__(self):
        super().__init__("Forest", "You are in a dark forest filled with tall trees and distant sounds.", ["Explore", "Fight", "Talk"])

class Castle(Location):
    def __init__(self):
        super().__init__("Castle", "You stand before a grand castle with high walls and a heavy gate.", ["Explore", "Fight", "Talk"])

class Village(Location):
    def __init__(self):
        super().__init__("Village", "A peaceful village with friendly locals and bustling markets.", ["Explore", "Fight", "Talk"])
