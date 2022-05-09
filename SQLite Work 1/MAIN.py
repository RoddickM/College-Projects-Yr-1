# Imports the FUNCTIONS python file and the SQLite module
from FUNCTIONS import *
import sqlite3

# Connects to the data file
conn = sqlite3.connect("sport.db")

'''
The loop below allows the user to enter the following parameters to the database:
ID
First name
Last name
Age
Favourite sport
Whether they play said sport

And it will keep going until the user wants it to stop
'''
while True:
    sport_id = num_validation("Enter person ID: ")
    sport_first_name = length_validation("Type in your first name: ")
    sport_last_name = length_validation("Type in your last name: ")
    sport_age = num_validation("Type in your age: ")
    fav_sport = character_val("What is your favourite sport: ")
    sport_play = y_n_true_false("Do you play your favourite sport?(Y/N): ")

    # converts the input from Y or N to True or False
    if sport_play == "y" or "Y":
        sport_play = "True"
    elif sport_play == "n" or "N":
        sport_play = "False"

    # inserts data to SQL data
    conn.execute('''
    INSERT INTO SPORT(ID, FIRST_NAME, LAST_NAME, AGE, FAV_SPORT, PLAY_SPORT)
    VALUES (?,?,?,?,?,?)''', (sport_id, sport_first_name, sport_last_name, sport_age, fav_sport, sport_play))
    conn.commit()

    # lets user add more data or stop program
    choice = input("\nAdd another record?(Y/N): ")
    if choice == "N" or "n":
        break
    else:
        continue

# shows that the data has been entered successfully
print("\nData has been entered")

# makes sure that the data selected is in one variable
display_data = conn.execute("SELECT ID, FIRST_NAME, LAST_NAME, AGE, FAV_SPORT, PLAY_SPORT from SPORT")

# loops through the rows in the SQL file and display the data to a specific format (display_format)
for row in display_data:
    display_format = f"\nID: {row[0]}"
    display_format += f"\nFirst name: {row[1]}"
    display_format += f"\nLast name: {row[2]}"
    display_format += f"\nAge: {row[3]}"
    display_format += f"\nFavourite sport: {row[4]}"
    display_format += f"\nPlay favourite sport: {row[5]}"
    # prints the all the data and its preferred format
    print(display_format)
