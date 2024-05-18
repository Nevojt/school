from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu import Menu

coffee_maker = CoffeeMaker()
menu = Menu()
money = MoneyMachine()

# print(coffee_maker.report())
# print(money.report())
# while True:

#     print(f"Menu:\n{menu.get_items()}")

#     user_choice = input("How is choice drink? ")
#     if user_choice == "report":
#         coffee_maker.report()
#         money.report()
#     else:

#         find_drink = menu.find_drink(user_choice)
#         expect_resource = coffee_maker.is_resources(find_drink)
#         if expect_resource == True:
#             coins = money.process_coins()
#             result = money.make_payment(coins)
            
#             if result:
#                 coffee_maker.make_coffee(find_drink)
#         else:
#             break

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