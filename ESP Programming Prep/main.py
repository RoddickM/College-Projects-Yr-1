from validation import *
import pandas as pd
df = pd.read_csv("house_prices.csv")


def main_menu():
    display_menu = "Welcome to Newhaven Property Investment Property Search"
    display_menu += "\nPlease type in the number next to the action you wish to do"
    display_menu += "\n[1] Search for a property"
    display_menu += "\n[2] Sort Properties"
    display_menu += "\n[3] Display Graph"
    display_menu += "\n[4] Exit"
    print(display_menu)
    choose_function = int_range_check("Type the number here: ", 1, 4)

    if choose_function == 1:
        house_search()
    elif choose_function == 2:
        sort_properties()
    elif choose_function == 3:
        display_graph()
    else:
        exit("See you again soon!")


def house_search():

    print(df.value_counts("Area"))


def sort_properties():
    pass


def display_graph():
    pass
