class Location:
    def __init__(self, name, opis, działania):
        self.name = name
        self.opis= opis
        self.działania = działania

class basement(Location):
    def __init__(self):
        super().__init__("besement", "You are in dark basement.", ["Explore", "Talk"])

class house(Location):
    def __init__(self):
        super().__init__("house", "You are standing in front of a big house.", ["Explore", "Talk"])

class city(Location):
    def __init__(self):
        super().__init__("city", "A quiet city with nice markets", ["Explore", "Talk"])