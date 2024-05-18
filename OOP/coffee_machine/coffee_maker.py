class CoffeeMaker:
    #  Модель машини яка робить каву
    def __init__(self) -> None:
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }
        
    def report(self):
        # Відображаємо кількість ресурсів
        print(f"Water: {self.resources['water']} ml")
        print(f"Milk: {self.resources['milk']} ml")
        print(f"Coffee: {self.resources['coffee']} mg")
        
    def is_resources(self, drink):
        # Перевіряємо чи є достатньо ресурсів для приготування кави
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}")
                can_make = False
        return can_make
        
    def make_coffee(self, order):
        #  Віднімаємо інгредієнти коли робимо каву
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")