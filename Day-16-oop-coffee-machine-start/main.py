from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

c_menu = Menu()
money_mach = MoneyMachine()
coffe_maker = CoffeeMaker()

is_on = True
while is_on:
    choice = input(f"What would you like ({c_menu.get_items()})")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffe_maker.report()
        money_mach.report()
    else:
        order = c_menu.find_drink(choice)
        if coffe_maker.is_resource_sufficient(order) and money_mach.make_payment(order.cost):
            coffe_maker.make_coffee(order)


