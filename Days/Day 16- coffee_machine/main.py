from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

check_out = MoneyMachine()
coffee_maker = CoffeeMaker()
order_menu = Menu()

is_on = True

while is_on:
    user_choice = input(f"What would you like to have? {order_menu.get_items()} ").lower()
    if user_choice == "report":
        coffee_maker.report()
        check_out.report()
    elif user_choice == "off":
        is_on = False
    else:
        user_choice = order_menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(user_choice):
            check_out.make_payment(user_choice.cost)
            coffee_maker.make_coffee(user_choice)
            
