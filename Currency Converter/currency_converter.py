# imports the pandas library and validation file with validation functions
import pandas as pd
from validation import *


# menu for the currency converter with 8 currency conversion choices
def currency_converter_menu():
    display_menu = "\nPlease select from the following options:"
    display_menu += "\n[ 1 ] Pound Sterling (GBP) --> Euros (EUR)"
    display_menu += "\n[ 2 ] Euros (EUR) --> Pound Sterling (GBP)"
    display_menu += "\n[ 3 ] Pound Sterling (GBP) --> Australian Dollars (AUD)"
    display_menu += "\n[ 4 ] Australian Dollars (AUD) --> Pound Sterling (GBP)"
    display_menu += "\n[ 5 ] Pound Sterling (GBP) --> Japanese Yen (JPY)"
    display_menu += "\n[ 6 ] Japanese Yen (JPY) --> Pound Sterling (GBP)"
    display_menu += "\n[ 7 ] Pound Sterling (GBP) --> US Dollars (USD)"
    display_menu += "\n[ 8 ] US Dollars (USD) --> Pound Sterling (GBP)"
    print(display_menu)


# gets both the currency conversion details for conversion rates and their symbol
def get_currency(menu_choice):
    # currency conversion details for conversion rates in a dictionary
    # depending on your choice from the menu, different conversion details will be sent to the other functions
    currencies = {
        '1': 'GBP - EUR',
        '2': 'EUR - GBP',
        '3': 'GBP - AUD',
        '4': 'AUD - GBP',
        '5': 'GBP - JPY',
        '6': 'JPY - GBP',
        '7': 'GBP - USD',
        '8': 'USD - GBP'}

    # currency symbols details in a dictionary
    currency_symbols = {
        '1': '£ -> €',
        '2': '€ -> £',
        '3': '£ -> $',
        '4': '$ -> £',
        '5': '£ -> ¥',
        '6': '¥ -> £',
        '7': '£ -> $',
        '8': '$ -> £'}

    # gets the currency details and symbols from the two dictionaries
    currency_symbol = currency_symbols.get(menu_choice)
    currency_to_convert = currencies.get(menu_choice)

    # returns the details and symbols to variables in another functions
    return currency_to_convert, currency_symbol


# gets the conversion rate information
def get_conversion_rate(currency):
    # exports conversion details from teh csv file
    df = pd.read_csv("Task4a_data.csv")

    # it will extract the latest currency conversion rates from the csv file
    current_conversion_rate = df[currency].iloc[-1]

    # returns the conversion rates so that it can be stored in a variable
    return current_conversion_rate


# gets the amount the user wants to convert
def get_amount_to_convert(currency):
    # displays to the user what currency they are converting to
    print("\nYou are converting: ", currency)

    # allows the user to input their conversion rates with validation to make sure they enter only numbers and decimals
    amount_to_convert = float_validation("\nPlease enter the amount you wish to convert: ")

    # returns the amount the user wants to convert so that it can be stored in a variable
    return amount_to_convert


# the main function that does the conversion and displays it to the user
def perform_conversion(conversion_amount, conversion_rate, currency, currency_symbol):
    # the variable below calculates the converted amount from the user's input
    amount_received = round(conversion_amount * conversion_rate, 2)

    # the line of variables and print function below displays to the user:
    # what the user has converted from
    # what the converted amount is
    display_receipt = "\n---------------------------------------------------"
    display_receipt += f'\nYou are converting {currency_symbol[0]}{conversion_amount} in {currency[0:3]}'
    display_receipt += f'\nYou will receive {currency_symbol[5]}{amount_received} in {currency[6:9]}'
    display_receipt += "\n---------------------------------------------------"
    print(display_receipt)


# the function that connects all the functions above into a while loop so that the user can make multiple transactions
def currency_converter():
    # while loop to allo user to do multiple conversions
    while True:
        # displays currency converter menu
        currency_converter_menu()
        # asks the user for which conversion option they want to choose and storing it in a variable
        convert_choose = range_validation(
            "\nPlease type the number next to the currency conversion you want to do (1-8): ",
            start_range=1, end_range=8)

        # gets the currency rate colum details for the csv file and also currency symbol for the conversion
        # and storing it in two variables
        currency, currency_symbol = get_currency(convert_choose)

        # calculates the conversion rate and storing it in a variable
        conversion_rate = get_conversion_rate(currency)

        # asks the user for how much money they want to convert and storing it in a variable
        amount_to_convert = get_amount_to_convert(currency)

        # performs the conversion and also displaying the result
        perform_conversion(amount_to_convert, conversion_rate, currency, currency_symbol)

        # asks the user whether they want to do another conversion or go back to the main menu
        # this has validation to make sure the user only enter y or n in capitals or lower case
        restart = y_or_n_validation("\nDo you want to do another conversion?(Type Y/N): ")
        if restart == "Y" or restart == "y":
            # restarts the conversion process
            continue
        else:
            # breaks from the loop and back to the main menu
            print("")
            break
