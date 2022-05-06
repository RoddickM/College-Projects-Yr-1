# imports pandas module to manipulate the csv file
# imports the validation file with functions to validate user input
import pandas as pd
from validation import *


# all the processes is inserted into one big function with sub_functions inside them
def airline_comparator():
    while True:
        # the function below displays the travel destinations the user can choose to compare airlines for
        # this function was from the original code with some modifications
        def destination_menu():
            # displays the menu using print functions (from original code)
            print("\n\n######################################################")
            print("########         Choose a destination          ########")
            print("[ 1 ] Alicante")
            print("[ 2 ] Amsterdam")
            print("[ 3 ] Athens")
            print("[ 4 ] Budapest")
            print("[ 5 ] Cologne")
            print("[ 6 ] Dublin")
            print("[ 7 ] Munich")
            print("[ 8 ] Paris")
            print("[ 9 ] Rhodes")
            print("######################################################")

            # asks for user input for destination
            menu_choice = int_range_validation("Please type in the number next to your preferred destination: ", 1, 9)
            # list that will convert user input to destination
            airport_list = ["Alicante",
                            "Amsterdam",
                            "Athens",
                            "Budapest",
                            "Cologne",
                            "Dublin",
                            "Munich",
                            "Paris",
                            "Rhodes"]

            # the two pieces of code below converts the user input into one of the values from the list airport_list
            airport_position = menu_choice - 1
            return airport_list[airport_position]

        # collects the month that the user wishes to travel and validates input
        def get_date():
            while True:
                # uses string concatenation for display of menu
                # this code is from the original code given to us
                display = "\n\n######################################################"
                display += "\nWhen will you be traveling?"
                display += "\nPlease choose the number next to month you want to travel"
                display += "\n[ 1 ] January"
                display += "\n[ 2 ] February"
                display += "\n[ 3 ] March"
                display += "\n[ 4 ] April"
                display += "\n[ 5 ] May"
                display += "\n[ 6 ] June"
                display += "\n[ 7 ] July"
                display += "\n[ 8 ] August"
                display += "\n[ 9 ] September"
                display += "\n[ 10 ] October"
                display += "\n[ 11 ] November"
                display += "\n[ 12 ] December"
                display += "\n######################################################"
                print(display)

                # list that will convert user input to the months
                month_list = ["January",
                              "February",
                              "March",
                              "April",
                              "May",
                              "June",
                              "July",
                              "August",
                              "September",
                              "October",
                              "November",
                              "December"]

                # asks the user for a value they want to input
                month_choice = int_range_validation("Please enter the number of your choice (1 - 12): ", 1, 12)

                # converts use input to a value from the list month_list
                travel_date = month_list[month_choice-1]
                return travel_date

        # gets the main list of data that matches user search criteria and displays it
        # this was from the original code
        def get_data():
            # connects to csv file
            df = pd.read_csv("Task4a_data 1.csv")
            # extracts only the data with the user's preferred month and destination
            # also displays the airline and the price of the airline
            # does not display commission
            extract = df.loc[(df['Month'] == month) & (df['Destination'] == destination), df.columns != "Commission (%)"]
            # prints the all the data that had been extracted by the above variable
            print("\n\nWe have found these flights that match your criteria:")
            print(extract.to_string(index=False))
            # returns the data from the extract variable to be used later
            return extract

        # extracts more meaningful data from the results for comparison
        # this was from the original code
        def compare_data(data, chosen_destination, chosen_month):
            # gets the columns Airline and Price from the csv file
            compare_df = data[['Airline', 'Price']]

            # sorting the csv file so that it shows the highest and lowest values
            column = compare_df['Price']
            max_price = column.max()
            min_price = column.min()

            # displays the most expensive and least expensive flights as tables.
            most_expensive = compare_df.loc[(data['Price'] == max_price)]
            least_expensive = compare_df.loc[(data['Price'] == min_price)]

            # creates the average price and rounds it to 2 decimal places
            average_price = round(compare_df['Price'].mean(), 2)

            # displays the most expensive, least expensive and the average price for the destination
            print("\n\n###############################################")
            print("The most expensive flights to {} in {} are in GBP(£):".format(chosen_destination, chosen_month))
            print(most_expensive.to_string(index=False))
            print("\n")
            print("The least expensive flights to {} in {} are in GBP(£):".format(chosen_destination, chosen_month))
            print(least_expensive.to_string(index=False))
            print("\n")
            print("The average price of a flight to {} in {} is in GBP(£): ".format(chosen_destination, chosen_month))
            print(average_price)
            print("###############################################")

        # the code below is where all the run are run with variables connected to them
        # menu variable
        destination = destination_menu()
        # month variable
        month = get_date()
        # extracting data
        extracted_data = get_data()
        # highest and lowest price
        compare_data(extracted_data, destination, month)
        # asks the user if they want to restart
        restart_comparator = y_or_n_validation("\nDo you want to compare another destination?(Y/N): ")
        print("")
        # this will restart the fil and allow them to compare prices again
        if restart_comparator == "y" or restart_comparator == "Y":
            continue
        # this returns the user to the main menu
        else:
            break
