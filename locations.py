class Location:
    def __init__(self, name, description, enemies=None, items=None):
        self.name = name
        self.description = description
        self.enemies = enemies or []
        self.items = items or []

    def explore(self):
        if self.items:
            found_item = self.items.pop()
            return f'Znalazłeś {found_item}!', found_item
        else:
            return f'Nic nie znalazłeś', None


class Village(Location):
    def __init__(self):
        super().__init__(
            name="Wioska", 
            description="Wioska pełna mieszkańców.", 
            items=["Health potion", "Apple", "Cherries"])

class Forest(Location):
    def __init__(self):
        super().__init__(
            name="Las", 
            description="Ciemny, tajemniczy las pełen niespodzianek", 
            enemies=["Gremlin", "Dark elf", "Evil wolf"], 
            items=["Sword", "Bow", "Herbs"])

class Castle(Location):
    def __init__(self):
        super().__init__(
            name="Zamek",
            description="Opuszczony zamek pełen basniowych potworów",
            enemies=["Black knight", "Medusa", "Cerber"]
            items=["Shield", "Gold", "Helmet"]

        )


