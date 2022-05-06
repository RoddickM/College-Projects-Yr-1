# imports the pandas module for csv manipulation
# imports the matplotlib module for creating graphs
# imports validation to validate user input
import pandas as pd
import matplotlib.pyplot as plt
from validation import *

# connects to csv file
df = pd.read_csv("Task4a_data 1.csv")


# main variable for the whole program to run
def popular_destinations():
    # while loop allowing user to create multiple charts
    while True:
        # displays the months the user can choose to see the most popular file
        def month_menu():
            display = "\n\nPlease choose the number next to the month you want to find the most popular destination"
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
            display += "\n[ 13 ] All year"
            print(display)

            # list that will convert the user input to a value
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
                          "December",
                          "All year"]

            # asks the user to input a number
            month_choice = int_range_validation("Please enter the number of your choice (1 - 12): ", 1, 13)

            # converts the user input to a variable from the list month_list
            chosen_date = month_list[month_choice - 1]
            # returns the value that has been converted
            return chosen_date

        # creates the bar chart by month
        def create_chart_by_month():
            # gets the values from the month and destination column from the csv file
            popular_destination = df.loc[(df["Month"] == month), df.columns == "Destination"].value_counts()
            # controls the size of how big the bar chart will be displayed initially
            plt.figure(figsize=(15, 15))
            # creates the x and y-axis for the bar chart
            x_axis = []
            y_axis = []
            # uses for loops to insert values from the csv files to the lists in the code
            for i in popular_destination.index:
                for destination in list(i):
                    x_axis.append(destination)
            for i in popular_destination:
                y_axis.append(i)

            # displays the labels and titles for the bar chart
            plt.title(f"Most popular destination in {month}")
            plt.xlabel("Destinations")
            plt.ylabel("Number of visits")

            # plots the bar chart
            plt.bar(x_axis, y_axis)
            # rotates the x-labels to make it mre readable
            plt.xticks(rotation=60)
            # shows the bar chart
            plt.show()

        def create_chart_all_year():
            # gets the values from the month and destination column from the csv file
            count = df[["Destination"]].value_counts()
            # controls the size of how big the bar chart will be displayed initially
            plt.figure(figsize=(15, 15))
            # creates the x and y-axis for the bar chart
            x_axis = []
            y_axis = []
            # uses for loops to insert values from the csv files to the lists in the code
            for i in count.index:
                for destination in list(i):
                    x_axis.append(destination)
            for i in count:
                y_axis.append(i)

            # displays the labels and titles for the bar chart
            plt.title(f"Most popular destination all year")
            plt.xlabel("Destinations")
            plt.ylabel("Number of visits")

            # plots the bar chart
            plt.bar(x_axis, y_axis)
            # rotates the x-labels to make it mre readable
            plt.xticks(rotation=60)
            # shows the bar chart
            plt.show()

        # displays menu and asks for a month from the user
        month = month_menu()
        # if and else determines whether the user wants the data for the whole year or for only a specific month
        # displays chart for the whole year
        if month == "All year":
            print("\nDisplaying bar chart...")
            create_chart_all_year()
        # displays chart for a specific month
        else:
            print("\nDisplaying bar chart...")
            create_chart_by_month()

        # asks the user if they want to restart
        restart_popular_destination = y_or_n_validation("\nDo you want to display another chart?(Y/N): ")
        print("")
        # this will restart the fil and allow them to view popular destinations again
        if restart_popular_destination == "y" or restart_popular_destination == "Y":
            continue
        # this returns the user to the main menu
        else:
            break
