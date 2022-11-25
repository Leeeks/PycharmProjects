MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

coffee_machine_off = False
ready_for_operation = True


def report():
    print(
        f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}")


def check_resources(drink):
    if int(MENU[drink]["ingredients"]["water"]) > int(resources["water"]):
        print("Sorry there is not enough water.")
        return False
    elif int(MENU[drink]["ingredients"]["milk"]) > int(resources["milk"]):
        print("Sorry there is not enough milk.")
        return False
    elif int(MENU[drink]["ingredients"]["coffee"]) > int(resources["coffee"]):
        print("Sorry there is not enough coffee.")
        return False
    else:
        return True


def process_coins():
    print("Please insert coins.")
    quarters = int(input("how many quarters?"))
    dimes = int(input("how many dimes?"))
    nickles = int(input("how many nickles?"))
    pennies = int(input("how many pennies?"))
    monetary_value = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    return float(monetary_value)


def make_coffee(drink):
    for ingredient in MENU[drink]["ingredients"]:
        resources[ingredient] = int(resources[ingredient]) - int(MENU[drink]["ingredients"][ingredient])


def check_transaction(drink, money):
    if MENU[drink]["cost"] > money:
        print("Sorry that's not enough money.")
        return False
    elif MENU[drink]["cost"] < money:
        resources["money"] = float(resources["money"]) + float(MENU[drink]["cost"])
        change = money - MENU[drink]["cost"]
        change = round(change, 2)
        print(f"Here is ${change} in change.\nHere is your {drink} ☕. Enjoy!")
        return True
    elif MENU[drink]["cost"] == money:
        resources["money"] = float(resources["money"]) + float(MENU[drink]["cost"])
        print(f"Here is your {drink} ☕. Enjoy!")
        return True


while not coffee_machine_off:
    ready_for_operation = True
    while ready_for_operation:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ")
        if user_choice == "off":
            coffee_machine_off = True
            break
        elif user_choice in MENU:
            if not check_resources(user_choice):
                ready_for_operation = False
                break
            if not check_transaction(user_choice, process_coins()):
                ready_for_operation = False
                break
            make_coffee(user_choice)

        elif user_choice == "report":
            report()
        else:
            print("This is not a valid choice. Please try again.")
