from machine_data import *


# TODO: 3.refund or give the change
def manage_order(drink_ordered, payed):
    if payed < MENU[drink_ordered]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return 0
    else:
        manage_resources(drink_ordered)
        change = payed - MENU[drink_ordered]["cost"]
        print(f"Here is ${round(change,2)} in change. \nHere is your {drink_ordered} ☕️. Enjoy!")
        return MENU[drink_ordered]["cost"]


# TODO: 2. ask user to insert coins
def calculate_payment():
    print("Please insert coins.")
    num_quarters = int(input("how many quarters?: "))
    num_dimes = int(input("how many dimes?: "))
    num_nickles = int(input("how many nickles?: "))
    num_pennies = int(input("how many pennies?: "))
    payed_money = num_quarters * 0.25 + num_dimes * 0.1 + num_nickles * 0.05 + num_pennies * 0.01
    return payed_money


# TODO: 4. increase or decrease the values based on the orders
def manage_resources(drink_ordered):
    resources["water"] -= MENU[drink_ordered]["ingredients"]["water"]
    resources["coffee"] -= MENU[drink_ordered]["ingredients"]["coffee"]
    if drink_ordered != 'espresso':
        resources["milk"] -= MENU[drink_ordered]["ingredients"]["milk"]


# TODO: 5. publish the report
def show_report(stored_money):
    print("Water : " + str(resources["water"]) + "ml")
    print("Milk : " + str(resources["milk"]) + "ml")
    print("Coffee : " + str(resources["coffee"]) + "g")
    print(f"Money : ${stored_money}")


# TODO: 6. check if we have enough resources
def check_availability(drink_ordered):
    for key in MENU[drink_ordered]["ingredients"]:
        if MENU[drink_ordered]["ingredients"][key] > resources[key]:
            print(f"Sorry, we run out of {key}")
            return 0
        else:
            return 1


order = ''
money = 0
while order != 'off':
    # TODO: 1. ask user to put his order
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == 'report':
        show_report(money)
    elif order == 'espresso' or order == 'latte' or order == 'cappuccino':
        if check_availability(order):
            payment = calculate_payment()
            money += manage_order(order, payment)
