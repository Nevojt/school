class MenuItems:
    # Створюємо меню
    def __init__(self, name, water, milk, coffee, cost) -> None:
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }
        
class Menu:
    # Модель меню напоїв
    def __init__(self) -> None:
        self.menu = [
            MenuItems(name="Late", water=200, milk=150, coffee=24, cost=2.5),
            MenuItems(name="Espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItems(name="Cappuccino", water=250, milk=50, coffee=24, cost=3)
        ]
        
    def get_items(self):
        #  Повертаємо назву напоїв які ми пропонуємо користувачеві
        options = ""
        for item in self.menu:
            options += f"{item.name}: ${item.cost}\n"
    
        return options
    
    def find_drink(self, order_name):
        #  Повертаємо об'єкт напою який ми пропонуємо користувачеві, якщо такого напою не має сповіщаємо користувача про це
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available")