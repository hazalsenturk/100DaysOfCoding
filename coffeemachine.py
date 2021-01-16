MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
}

coffee_mug = """
      )  (
     (   ) )
      ) ( (
 mrf_______)_
 .-'---------|
( C|/\/\/\/\/|
 '-./\/\/\/\/|
   '_________'
    '-------'
"""

# TODO-3: Print report.


def print_report(resources):
    """Reports the remained resources"""

    print(f"Water: {resources['water']} \nMilk: {resources['milk']} \nCoffee: {resources['coffee']}")

# TODO-4: Check resources sufficient? Refill


def check_resource(choice_recipe, resources, choice_price, user_choice):
    """Check the ingredients needed for user_choice against the machine sources"""

    if choice_recipe['water'] > resources['water']:
        print("Sorry there is not enough water. Call the service provider. ")
        return
    elif 'milk' in choice_recipe and choice_recipe['milk'] > resources['milk']:
        print("Sorry there is not enough milk. Call the service provider. ")
        return
    elif choice_recipe['coffee'] > resources['coffee']:
        print("Sorry there is not enough coffee. Call the service provider")
        return
    else:
        process_coins(user_choice, choice_price)
        make_coffee(choice_recipe, resources)


# TODO-6: Check transaction successful?

def process_coins(user_choice, choice_price):

    """ Calculates the total coins inserted,
    if there is enough money for the choice proceed for recipe otherwise return False"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    coin_inserted = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies

    if choice_price > coin_inserted:
        print("Sorry that's not enough money. Money refunded.")
        return
    else:
        change_return = round(coin_inserted - choice_price, 2)
        if change_return > 0:
            print(f"Here is ${change_return} in change. ")
            print(f"Here is your {user_choice} ☕️ Enjoy! \n")


# TODO-7: Make Coffee

def make_coffee(choice_recipe, resources):
    """Reducts the recipe amounts from the resources of the machine"""

    resources["water"] -= choice_recipe["water"]
    if 'milk' in choice_recipe:
        resources["milk"] -= choice_recipe["milk"]
    resources["coffee"] -= choice_recipe["coffee"]
    # print(resources)
    return resources

# TODO-8: Combine functions in the game


is_machine_on = True
print(coffee_mug)

while is_machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino) ").lower()
    if user_choice == "off":
        is_machine_on = False
    elif user_choice == "report":
        print_report(resources)
    else:
        choice_recipe = MENU[user_choice]['ingredients']
        choice_price = MENU[user_choice]['cost']
        # print(choice_recipe)
        check_resource(choice_recipe, resources, choice_price, user_choice)
