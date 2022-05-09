import pandas as pd
import matplotlib.pyplot as plt
import time
from Task4a_flight_prices import *
import numpy as np


def popular_destination():
    # class with colours as objects to use throughout the code
    def menu_pop():

        class Bcolors:
            BLUE = '\033[94m'
            CYAN = '\033[96m'
            RED = '\033[91m'
            END = '\033[0m'
            BOLD = '\033[1m'
        print(70*"~")
        print("Here are some graphs to show the most popular destinations", 15*"~")
        print("Please choose an option from the menu below", 10*"~")
        print(Bcolors.CYAN + "[" + Bcolors.END, "1", Bcolors.CYAN + "]" + Bcolors.END + "Pie Chart")
        print(Bcolors.CYAN + "[" + Bcolors.END, "2", Bcolors.CYAN + "]" + Bcolors.END + "Bar Chart")
        print(Bcolors.CYAN + "[" + Bcolors.END, "3", Bcolors.CYAN + "]" + Bcolors.END + "Exit ")
        while True:
            try:
                choice_main = int(input("Enter an option: \n>> "))
                if 0 < choice_main < 4:
                    break

                else:
                    print(Bcolors.RED + "Invalid Entry. Please enter a number between 1-3" + Bcolors.END)

            except ValueError:
                print(Bcolors.RED + "Invalid Entry. Please enter a number" + Bcolors.END)

        if choice_main == 1:
            fig = plt.figure(figsize=(30, 30))
            csv = pd.read_csv('Task4a_data.csv')
            data = csv[['Destination']]

            plt.title("Destinations in order of popularity)")
            y = data['Destination'].value_counts()
            plt.xlabel("Destinations")
            plt.ylabel("Popularity in figures")
            my_labels = data['Destination'].value_counts().keys().tolist()
            explode = [0.1, 0.05, 0, 0, 0, 0, 0, 0, 0]

            plt.pie(y, labels=my_labels, explode=explode, autopct='%1.1f%%')
            plt.show()
            menu_pop()

        elif choice_main == 2:
            fig = plt.figure(figsize=(30, 30))
            csv = pd.read_csv('Task4a_data.csv')
            data = csv[['Destination']]
            # defining the x and y-axis
            x = data['Destination'].value_counts().keys().tolist()
            y = data['Destination'].value_counts()
            plt.title("Destinations in order of popularity)")
            # plotting the graph
            plt.bar(x, y)
            plt.xlabel("Destinations")
            plt.ylabel("Popularity in figures")
            plt.show()
            time.sleep(0.5)
            menu_pop()
        elif choice_main == 3:
            print(Bcolors.RED + "Exiting..." + Bcolors.END)
            main_menu()
    menu_pop()


def commission_earned():

    class Bcolors:
        BLUE = '\033[94m'
        CYAN = '\033[96m'
        RED = '\033[91m'
        END = '\033[0m'
        BOLD = '\033[1m'
    # menu to display the commission earned by airline
    print(70 * "~")
    print("Here are some graphs to show the commission earned from the sales from these airlines", 15 * "~")
    print("Please choose an option from the menu below", 10 * "~")
    print(Bcolors.CYAN + "[" + " 1 " + "]" + Bcolors.END + "JetWay")
    print(Bcolors.CYAN + "[" + " 2 " + "]" + Bcolors.END + "Barry Air")
    print(Bcolors.CYAN + "[" + " 3 " + "]" + Bcolors.END + "Super Jet")
    print(Bcolors.CYAN + "[" + " 4 " + "]" + Bcolors.END + "Yorkshire")
    print(Bcolors.CYAN + "[" + " 5 " + "]" + Bcolors.END + "Lift")
    print(Bcolors.CYAN + "[" + " 6 " + "]" + Bcolors.END + "Compare all the commissions earned by all the airlines")
    print(Bcolors.CYAN + "[" + " 7 " + "]" + Bcolors.END + "Exit ")
    # global jw_total_commission
    # global ba_total_commission
    # global sj_total_commission
    # global yk_total_commission
    # global li_total_commission
    # data validation for the choice of the user
    while True:
        try:
            choice_airline = int(input("Enter an option: \n>> "))
            if 0 < choice_airline < 8:
                break
            else:
                print(Bcolors.RED + "Invalid Entry. Please enter a number between 1-7" + Bcolors.END)
        except ValueError:
            print(Bcolors.RED + "Invalid Entry. Please enter a number" + Bcolors.END)

    #################################################################
    # this is to display some analytics and graphs for JetWay airline
    if choice_airline == 1:

        # calculating the commission earned for the jetway airline for the whole year
        commission_airline = "JetWay"
        df = pd.read_csv('Task4a_data.csv')
        extract_comm = df.loc[(df["Airline"] == "JetWay"), df.columns != "Airline"]
        extract_comm["Commission Earned"] = round(extract_comm["Price"] * (extract_comm["Commission (%)"] / 100), 2)
        comm_calculated = extract_comm.to_string(index=False)
        jw_total_commission = round(extract_comm["Commission Earned"].sum(), 2)
        print("Here is a breakdown of the commissions earned by {}.".format(commission_airline))
        print(comm_calculated)
        print('The total commission earned for {} was £{}.'.format(commission_airline, jw_total_commission))
        commission_earned()

    #################################################################
    # this is to display some analytics and graphs for Barry Air airline
    elif choice_airline == 2:

        # calculating the commission earned for the Barry air airline
        commission_airline = "Barry Air"
        df = pd.read_csv('Task4a_data.csv')
        extract_comm = df.loc[(df["Airline"] == commission_airline), df.columns != "Airline"]
        extract_comm["Commission Earned"] = round(extract_comm["Price"] * (extract_comm["Commission (%)"] / 100), 2)
        comm_calculated = extract_comm.to_string(index=False)
        ba_total_commission = round(extract_comm["Commission Earned"].sum(), 2)
        print("Here is a breakdown of the commissions earned by {}.".format(commission_airline))
        print(comm_calculated)
        print('The total commission earned by {} was £{}.'.format(commission_airline, ba_total_commission))
        commission_earned()

    #################################################################
    # this is to display some analytics and graphs for Super Jet airline
    elif choice_airline == 3:
        # calculating the commission earned for the super Jet airline
        commission_airline = "Super Jet"
        df = pd.read_csv('Task4a_data.csv')
        extract_comm = df.loc[(df["Airline"] == commission_airline), df.columns != "Airline"]
        extract_comm["Commission Earned"] = round(extract_comm["Price"] * (extract_comm["Commission (%)"] / 100), 2)
        comm_calculated = extract_comm.to_string(index=False)
        sj_total_commission = round(extract_comm["Commission Earned"].sum(), 2)
        print("Here is a breakdown of the commissions earned by {}.".format(commission_airline))
        print(comm_calculated)
        print('The total commission earned for {} was £{}.'.format(commission_airline, sj_total_commission))
        commission_earned()

    #################################################################
    # this is to display some analytics and graphs for Yorkshire airline
    elif choice_airline == 4:

        # calculating the commission earned for the Yorkshire airline
        commission_airline = "Yorkshire Airlines"
        df = pd.read_csv('Task4a_data.csv')
        extract_comm = df.loc[(df["Airline"] == commission_airline), df.columns != "Airline"]
        extract_comm["Commission Earned"] = round(
            extract_comm["Price"] * (extract_comm["Commission (%)"] / 100), 2)
        comm_calculated = extract_comm.to_string(index=False)
        yk_total_commission = round(extract_comm["Commission Earned"].sum(), 2)
        print("Here is a breakdown of the commissions earned by {}.".format(commission_airline))
        print(comm_calculated)
        print('The total commission earned for {} was £{}.'.format(commission_airline, yk_total_commission))
        commission_earned()

    #################################################################
    # this is to display some analytics and graphs for Lift airline
    elif choice_airline == 5:
        # calculating the commission earned for the Lift airline
        commission_airline = "Lift"
        df = pd.read_csv('Task4a_data.csv')
        extract_comm = df.loc[(df["Airline"] == commission_airline), df.columns != "Airline"]
        extract_comm["Commission Earned"] = round(
            extract_comm["Price"] * (extract_comm["Commission (%)"] / 100), 2)
        comm_calculated = extract_comm.to_string(index=False)
        li_total_commission = round(extract_comm["Commission Earned"].sum(), 2)
        print("Here is a breakdown of the commissions earned by {}.".format(commission_airline))
        print(comm_calculated)
        print('The total commission earned for {} was £{}.'.format(commission_airline, li_total_commission))
        commission_earned()

    elif choice_airline == 6:
        print(Bcolors.BOLD + "How would like to display the graphs?")
        print(Bcolors.CYAN + "[" + Bcolors.END, "1", Bcolors.CYAN + "]" + Bcolors.END + "Pie chart")
        print(Bcolors.CYAN + "[" + Bcolors.END, "2", Bcolors.CYAN + "]" + Bcolors.END + "Histograms (bar plot)")
        print(Bcolors.CYAN + "[" + Bcolors.END, "3", Bcolors.CYAN + "]" + Bcolors.END + "Exit ")
        while True:

            try:
                choice_graph = int(input("Enter an option: "))
                if 0 < choice_graph < 4:
                    break

                else:
                    print(Bcolors.RED + "Invalid Entry. Please enter a number between 1-3" + Bcolors.END)

            except ValueError:
                print(Bcolors.RED + "Invalid Entry. Please enter a number" + Bcolors.END)

        df = pd.read_csv('Task4a_data.csv')
        extract_comm = df.loc[(df["Airline"] == "JetWay"), df.columns != "Airline"]
        extract_comm["Commission Earned"] = round(extract_comm["Price"] * (extract_comm["Commission (%)"] / 100), 2)
        comm_calculated = extract_comm.to_string(index=False)
        jw_total_commission = round(extract_comm["Commission Earned"].sum(), 2)

        extract_comm = df.loc[(df["Airline"] == "Barry Air"), df.columns != "Airline"]
        extract_comm["Commission Earned"] = round(extract_comm["Price"] * (extract_comm["Commission (%)"] / 100), 2)
        comm_calculated = extract_comm.to_string(index=False)
        ba_total_commission = round(extract_comm["Commission Earned"].sum(), 2)

        extract_comm = df.loc[(df["Airline"] == "Super Jet"), df.columns != "Airline"]
        extract_comm["Commission Earned"] = round(extract_comm["Price"] * (extract_comm["Commission (%)"] / 100), 2)
        comm_calculated = extract_comm.to_string(index=False)
        sj_total_commission = round(extract_comm["Commission Earned"].sum(), 2)

        extract_comm = df.loc[(df["Airline"] == "Yorkshire Airlines"), df.columns != "Airline"]
        extract_comm["Commission Earned"] = round(extract_comm["Price"] * (extract_comm["Commission (%)"] / 100), 2)
        comm_calculated = extract_comm.to_string(index=False)
        yk_total_commission = round(extract_comm["Commission Earned"].sum(), 2)

        extract_comm = df.loc[(df["Airline"] == "Lift"), df.columns != "Airline"]
        extract_comm["Commission Earned"] = round(extract_comm["Price"] * (extract_comm["Commission (%)"] / 100), 2)
        comm_calculated = extract_comm.to_string(index=False)
        li_total_commission = round(extract_comm["Commission Earned"].sum(), 2)

        # defining labels
        commission_fees = [jw_total_commission, ba_total_commission, sj_total_commission, yk_total_commission,
                           li_total_commission]
        airlines = ['Jet Way', 'Barry Air', 'Super Jet', 'Yorkshire Airlines', 'Lift']

        if choice_graph == 1:
            print("PROGRAMMER TO CREATE CODE FOR PIE CHART TO GO HERE")

        elif choice_graph == 2:
            commission_fees = [jw_total_commission, ba_total_commission, sj_total_commission, yk_total_commission,
                               li_total_commission]
            airlines = ['Jet Way', 'Barry Air', 'Super Jet', 'Yorkshire Airlines', 'Lift']
            # list of colours
            new_colors = ['green', 'blue', 'purple', 'brown', 'teal']
            # plotting graph
            plt.bar(airlines, commission_fees, color=new_colors)
            # adding legends to the graph with titles
            plt.title('Commissions earned by each airline agency', fontsize=14)
            plt.xlabel('Airlines', fontsize=14)
            plt.ylabel('Commission in £', fontsize=14)
            plt.grid(True)
            # show the graph
            plt.show()

        elif choice_graph == 3:
            print(Bcolors.RED + "Exiting..." + Bcolors.END)
            exit()


def main_menu():
    class Bcolors:
        BLUE = '\033[94m'
        CYAN = '\033[96m'
        RED = '\033[91m'
        END = '\033[0m'
        BOLD = '\033[1m'
    print(30*"~", "Welcome to Qwik Travel LTD", 30*"~")
    print("Choose an option", 10*"~")
    print(Bcolors.CYAN + "[" + Bcolors.END, "1", Bcolors.CYAN + "]" + Bcolors.END +
          "Choose a destination and compare prices of flights")
    print(Bcolors.CYAN + "[" + Bcolors.END, "2", Bcolors.CYAN + "]" + Bcolors.END +
          "Display graphs for most popular destinations")
    print(Bcolors.CYAN + "[" + Bcolors.END, "3", Bcolors.CYAN + "]" + Bcolors.END +
          "Display commission earned from sales from different airlines")
    print(Bcolors.CYAN + "[" + Bcolors.END, "4", Bcolors.CYAN + "]" + Bcolors.END + "Exit ")

    while True:
        try:
            choice_main = int(input("Enter an option: "))
            if 0 < choice_main < 5:
                break
            else:
                print(Bcolors.RED + "Invalid Entry. Please enter a number between 1-4" + Bcolors.END)
        except ValueError:
            print(Bcolors.RED + "Invalid Entry. Please enter a number" + Bcolors.END)

    if choice_main == 1:
        comparison()
    elif choice_main == 2:
        popular_destination()
    elif choice_main == 3:
        commission_earned()
    elif choice_main == 4:
        print(Bcolors.RED + "Exiting..." + Bcolors.END)
        exit()



