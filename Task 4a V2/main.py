# imports two modules from other files
# airline_comparator for comparing airline prices for a certain destination
# popular_destinations for creating bar charts that show the most popular destinations for a certain month/all year.
from airline_comparator import *
from popular_destinations import *
from comission_earned import *


# the function to display the main menu
# it uses variables and string concatenation instead of one variable
def main_menu():
    display = "Welcome to Qwik Travel LTD Holiday Comparator"
    display += "\n[ 1 ] Compare flight prices by month"
    display += "\n[ 2 ] Find out the most popular destination"
    display += "\n[ 3 ] Commission earned from sales from different airlines"
    display += "\n[ 4 ] Exit"
    print(display)


# the main loop that shows the options that redirects the program to other files
while True:
    # displays the main menu
    main_menu()
    # asks the user what option they would like to choose
    choose_option = int_range_validation("Type in the number next to the action you want to perform: ", 1, 4)
    # redirects to airline_comparator file
    if choose_option == 1:
        airline_comparator()
    # redirects to popular destinations file
    elif choose_option == 2:
        popular_destinations()
    # redirects to comission_earned file
    # this file is incomplete, so it doesn't do anything just yet
    elif choose_option == 3:
        view_raw_comission_data()
    # this exits the program with a message
    else:
        exit("Thank you for using our services!!")
