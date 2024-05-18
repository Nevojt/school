from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu import Menu

coffee_maker = CoffeeMaker()
menu = Menu()
money = MoneyMachine()


is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like?\n{options}")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resources(drink) and money.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)