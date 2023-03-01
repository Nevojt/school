from data import MENU
from data import resources


def report_status():
    """
    Shows the remaining resources
    """
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    moneys = resources["moneys"]
    return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${moneys}"


def menu_coffee():
    """
    The price of the selected drink
    """
    global cost_coffee

    if user_input == "espresso":
        cost_coffee = MENU["espresso"]["cost"]
        return f"The price of your coffee is ${cost_coffee}"
    elif user_input == "latte":
        cost_coffee = MENU["latte"]["cost"]
        return f"The price of your coffee is ${cost_coffee}"
    elif user_input == "cappuccino":
        cost_coffee = MENU["cappuccino"]["cost"]
        return f"The price of your coffee is ${cost_coffee}"


def resource_func():
    """
    Checks whether there are enough resources to prepare the drink
    if so, used them
    """
    if user_input == "espresso":
        if resources["water"] < 50 or resources["coffee"] < 18:
            print("Sorry, no resources 😔")
            return False
        else:
            resources["water"] -= 50
            resources["coffee"] -= 18
            resources["moneys"] += 1.50

    elif user_input == "latte":
        if resources["water"] < 200 or resources["coffee"] < 24 or resources["milk"] < 150:
            print("Sorry, no resources for latte 😔")
            return False
        else:
            resources["water"] -= 200
            resources["coffee"] -= 24
            resources["milk"] -= 15
            resources["moneys"] += 2.50

    elif user_input == "cappuccino":
        if resources["water"] < 250 or resources["coffee"] < 24 or resources["milk"] < 100:
            print("Sorry, no resources for cappuccino 😔")
            return False
        else:
            resources["water"] -= 250
            resources["coffee"] -= 24
            resources["milk"] -= 100
            resources["moneys"] += 3.0
    return True


def proces_money(money):
    """
    Checks whether there is enough money for a drink
    """
    change = money - cost_coffee
    if user_input == "espresso":
        if money >= MENU["espresso"]["cost"]:
            print(f"This is your balance: {change}")
            resource_func()
    elif user_input == "latte":
        if money >= MENU["latte"]["cost"]:
            print(f"This is your balance: {change}")
            resource_func()
    elif user_input == "cappuccino":
        if money >= MENU["cappuccino"]["cost"]:
            print(f"This is your balance: {change}")
            resource_func()
    else:
        print("Sorry, that's not enough money. ")


def input_coins():
    """
    Offers to deposit coins
    """
    money = 0
    print("Please insert coins.")

    quarters = int(input("how many quarters?: "))
    money += quarters * 0.25
    print(round(money, 2))

    dimes = int(input("how many dimes?: "))
    money += dimes * 0.10
    print(round(money, 2))

    nickles = int(input("how many nickles?: "))
    money += nickles * 0.05
    print(round(money, 2))

    pennies = int(input("how many pennies?: "))
    money += pennies * 0.01
    print(f"It's you money {round(money, 2)}")
    proces_money(money)


while True:
    user_input = input(" What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "report":
        print(report_status())
    elif user_input == "off":
        break
    elif user_input not in ["espresso", "latte", "cappuccino"]:
        print("Invalid input")
    else:
        print(menu_coffee())
        input_coins()
