# importing both the matplotlib pandas library to use for graphs
# also imports the validation file
import matplotlib.pyplot as plt
import pandas as pd
from validation import *

# calculates how big the size of the graph should be
plt.figure(figsize=(15, 20))
# connecting the program with the csv file
csv = pd.read_csv("Task4a_data.csv")
# extracting all the columns from the csv file
data = csv[["Date",
            "GBP - EUR",
            "EUR - GBP",
            "GBP - AUD",
            "AUD - GBP",
            "GBP - JPY",
            "JPY - GBP",
            "GBP - USD",
            "USD - GBP"]]


# currency rate menu with the same options as the currency conversion menu
def currency_rate_menu():
    display_menu = "\nChoose between the following currency rates that you want to find out: "
    display_menu += "\n[ 1 ] Pound Sterling (GBP) --> Euros (EUR)"
    display_menu += "\n[ 2 ] Euros (EUR) --> Pound Sterling (GBP)"
    display_menu += "\n[ 3 ] Pound Sterling (GBP) --> Australian Dollars (AUD)"
    display_menu += "\n[ 4 ] Australian Dollars (AUD) --> Pound Sterling (GBP)"
    display_menu += "\n[ 5 ] Pound Sterling (GBP) --> Japanese Yen (JPY)"
    display_menu += "\n[ 6 ] Japanese Yen (JPY) --> Pound Sterling (GBP)"
    display_menu += "\n[ 7 ] Pound Sterling (GBP) --> US Dollars (USD)"
    display_menu += "\n[ 8 ] US Dollars (USD) --> Pound Sterling (GBP)"
    print(display_menu)


# the function below allows the user's choice to be converted into a column from the csv files
# the data is stored in a dictionary
def get_currency_rate(menu_choice):
    currency_rates = {
        '1': 'GBP - EUR',
        '2': 'EUR - GBP',
        '3': 'GBP - AUD',
        '4': 'AUD - GBP',
        '5': 'GBP - JPY',
        '6': 'JPY - GBP',
        '7': 'GBP - USD',
        '8': 'USD - GBP'}

    # gets the currency details from the dictionary
    currency_to_display = currency_rates.get(menu_choice)

    # returns said details so that it can be stored in a variable
    return currency_to_display


# displays data from specific columns of the csv file
def currency_graph_display(currency_rate):
    # extracts the date
    x = data["Date"]
    # extracts the currency rates from all the rows
    y = data[currency_rate]

    # writes the titles and labels of the graph
    plt.title(f"{currency_rate} Current Currency Rates")
    plt.xlabel("Dates")
    plt.ylabel(f"{currency_rate} Currency Rate")

    # plots the graph
    plt.plot(x, y)
    # rotate the labels on the x-axis to make them more readable
    plt.xticks(rotation=60)
    # displays the graph to the user
    plt.show()


# the function that connects all the above functions so that they can work together to create a graph
def currency_rate_checker():
    # while loop to allow user to display multiple graphs of their choice
    while True:
        # displays menu
        currency_rate_menu()
        # asks for which currency rate they ar looking for
        currency_rate_choice = range_validation(
            "\nPlease type the number next to the currency rate you want to find out (1-8): ",
            start_range=1, end_range=8)
        print("")

        # converts choice so that it connects to a column from the csv file amd storing it in a variable
        currency_rate = get_currency_rate(currency_rate_choice)
        # displays currency rates
        currency_graph_display(currency_rate)

        # gives the user a choice whether they want to see another graph or go back to main menu
        restart = y_or_n_validation("\nDo you want to do another currency rate check?(Type Y/N): ")
        if restart == "Y" or restart == "y":
            continue
        else:
            print("")
            break
