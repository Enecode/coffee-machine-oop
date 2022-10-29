from menu import Menu, MenuItem
from make_coffee import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

while is_on:
    options = menu.get_items()
    user_choice = str(input(f'What would you like?\nOptions: \nlatte \nespresso'
                            f'\ncappuccino: ')).strip().lower()
    if user_choice == 'off':
        print("THE END")
        quit()
        is_on = False
    elif user_choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif menu.find_drink(user_choice) is None:
        print('\033[31mError. Please choose an available option.\033]m')
    else:
        beverage = menu.find_drink(user_choice)
        sufficient_resources = coffee_maker.is_resources_surfficient(beverage)
        sufficient_money = money_machine.make_payment(beverage.cost)
        if sufficient_resources and sufficient_money:
            print('Done! Allow us to make your beverage now.')
            coffee_maker.make_coffee(beverage)
