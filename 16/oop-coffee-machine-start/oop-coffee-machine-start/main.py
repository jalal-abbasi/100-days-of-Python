from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()
menu = Menu()

is_on = True
while is_on:
    choice = input(f"What would you like? {menu.get_items()}: ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffeemaker.report()
        moneymachine.report()
    else:
        item = menu.find_drink(choice)
        if coffeemaker.is_resource_sufficient(item):
            if moneymachine.make_payment(item.cost):
                coffeemaker.make_coffee(item)





