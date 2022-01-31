# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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
}


def check_resources(key):
    if resources['water'] >= MENU[key]['ingredients']['water']:
        if resources['coffee'] >= MENU[key]['ingredients']['coffee']:
            if resources['milk'] >= MENU[key]['ingredients']['milk']:
                return True
    else:
        return False


money = 0
user_choice = "on"
while user_choice != "off":
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == 'report':
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: ${money}")
    elif user_choice == 'off':
        print("Machine has been switched off.")
    elif user_choice != 'espresso' and user_choice != 'latte' and user_choice != 'cappuccino':
        print("Invalid choice.")
    else:
        if not check_resources(user_choice):
            print("Sorry there is not enough ingredients, money refunded.")
        else:
            print("Please insert coins")
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickels = int(input("How many nickels? "))
            pennies = int(input("How many pennies? "))
            money_in_dollar = 0.25 * quarters + 0.10 * dimes + 0.05 * nickels + 0.01 * pennies
            if money_in_dollar < MENU[user_choice]['cost']:
                print("Sorry that's not enough money. Money refunded.")
            else:
                money += MENU[user_choice]['cost']
                if money_in_dollar > MENU[user_choice]['cost']:
                    change = round(money_in_dollar - MENU[user_choice]['cost'], 2)
                    print(f"Here is your change of ${change}")
                resources['milk'] -= MENU[user_choice]['ingredients']['milk']
                resources['water'] -= MENU[user_choice]['ingredients']['water']
                resources['coffee'] -= MENU[user_choice]['ingredients']['coffee']
                print(f"There you go! Enjoy your {user_choice}.")
