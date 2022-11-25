from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine_off = False
ready_for_operation = True

myCoffeeMaker = CoffeeMaker()
myMenu = Menu()
myMoneyMachine = MoneyMachine()

print(myCoffeeMaker.report())
print(myMenu.get_items())
print(myMenu.find_drink("espresso").ingredients)

while not coffee_machine_off:
    ready_for_operation = True
    while ready_for_operation:
        user_choice = input(f"What would you like? {myMenu.get_items()}: ")
        user_choice = user_choice.lower()
        if user_choice == "off":
            coffee_machine_off = True
            break
        elif user_choice == "report":
            myCoffeeMaker.report()
            myMoneyMachine.report()
        elif user_choice == myMenu.find_drink(user_choice).name:
            if not myCoffeeMaker.is_resource_sufficient(myMenu.find_drink(user_choice)):
                ready_for_operation = False
                break
            if not myMoneyMachine.make_payment(myMenu.find_drink(user_choice).cost):
                ready_for_operation = False
                break
            myCoffeeMaker.make_coffee(myMenu.find_drink(user_choice))


        else:
            print("This is not a valid choice. Please try again.")
