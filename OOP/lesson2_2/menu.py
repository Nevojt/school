
class MenuItems:
    def __init__(self, name, water, milk, coffee, cost) -> None:
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }
        
class Menu:
    def __init__(self) -> None:
        self.menu =[
            MenuItems(name="late", water=200, milk=150, coffee=24, cost=2.5),
            MenuItems(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItems(name="cappuccino", water=250, milk=50, coffee=24, cost=3)
        ]
        
    def get_items(self):
        options = ""
        for item in self.menu:
            options += f"{item.name}\n"
        print(options)  
        return options
        
prod = Menu()
prod.get_items()      