# Imports two other python files:
# currency_converter is for the currency converter program
# graph display for the currency rate program
from currency_converter import *
from currrency_rate_checker import *


# Prints the main menu of the program where users can choose whether they want to:
# convert a currency or check currency rates
def main_menu():
    main_menu_display = "Welcome to RBSX Currency Converter!!"
    main_menu_display += "\nPlease Select from the following options:"
    main_menu_display += "\n[ 1 ] Currency Converter"
    main_menu_display += "\n[ 2 ] Currency Rate Check"
    main_menu_display += "\n[ 3 ] Exit"
    print(main_menu_display)


# while loop that starts unless user exits the program
while True:
    # displays the main menu function
    main_menu()
    # asks user for a choice from the main menu
    choose_option = range_validation("Please type the number next the option you are interested in (1-3): ",
                                     start_range=1, end_range=3)
    # if-else statement redirects the user depending on their choice from the menu
    if choose_option == "1":
        # currency converter program
        currency_converter()
    elif choose_option == "2":
        # currency rate checker
        currency_rate_checker()
    else:
        # exits the program with a message
        exit("\nThank you for using our program!!")
