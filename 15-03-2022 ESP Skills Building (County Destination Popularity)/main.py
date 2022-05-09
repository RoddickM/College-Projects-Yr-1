# imports external modules:
#   pandas for analysing datasets
#   matplotlib.pyplot for plotting graphs
import pandas as pd
import matplotlib.pyplot as plt


# this functions validates whether the input from the user is a whle number
# this function uses a try-catch for the error
def int_validation(text):
    while True:
        try:
            user_input = int(input(text))
            return user_input
        except ValueError:
            print("\n[ERROR] Please only type in whole numbers")


# this function makes sure that the user input is within range of the what 
# the program accepts
def int_range_validation(text, start_range, end_range):
    while True:
        user_input = int_validation(text)
        if user_input in range(start_range, end_range + 1):
            return user_input
        else:
            print(f"\n[ERROR] Please only type in the numbers in the range of {start_range} to {end_range}")
    

# connects to the csv file
df = pd.read_csv("EstateAgents.csv")
# adds all the values of how many times the county appear in the file
count = df["County"].value_counts()

# empty lists for x and y axis of barchart
x = []
y = []

# adds number of visits to x variable
for i in count:
    y.append(i)

# adds county name to y variable
for i in count.index:
    x.append(i)

while True:
    # below are the variables that displays the options of the program
    menu_display = "Welcome to T-Level Estates"
    menu_display += "\nChoose the method you want to the display the most visited county"
    menu_display += "\n[ 1 ] Display as text"
    menu_display += "\n[ 2 ] Display as bar chart"
    menu_display += "\n[ 3 ] Display as scatter graph"
    menu_display += "\n[ 4 ] Display as pie chart"
    menu_display += "\n[ 5 ] Exit"
    # displays the menu
    print(menu_display)
    # asks the user what option they wish to choose
    choose = int_range_validation("Please type the number next to the action you want to take: ", 1, 5)
    print("")
    
    if choose == 1:
        # displays the most visited county by text
        print("Destination popularity by county:")
        print(count + "\n")
    elif choose == 2:
        # add titles and labels to the bar chart
        plt.title("Most popular county to be visited")
        plt.xlabel("County")
        plt.ylabel("Number of visits")
    
        # creates the bar chart
        plt.bar(x, y)
        # rotates the labels on the x-axis by 60 degrees
        plt.xticks(rotation=60)
        # displays bar chart
        plt.show()
    elif choose == 3:
        # adds titles and labels to the scatter graph
        plt.title("Most popular county to be visited")
        plt.xlabel("County")
        plt.ylabel("Number of visits")
    
        # creates the scatter graph
        plt.scatter(x, y)
        # rotates the labels on the x-axis by 60 degrees
        plt.xticks(rotation=60)
        # displays scatter graph
        plt.show()
    elif choose == 4:
        # adds titles and labels to the pie chart
        plt.title("Most popular county to be visited")
        # creates the pie chart
        plt.pie(y, labels=x, autopct='%1.1f%%')
        # makes sure that the window/tab it is displayed on is a square
        plt.axis("equal")
        # displays pie chart
        plt.show()
    elif choose == 5:
        # exits the program
        break
    
