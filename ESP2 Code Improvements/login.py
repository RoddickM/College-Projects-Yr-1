from main import *
from account_create import *


def login():
    print("Welcome to Qwik Travel Airline Comparator!")
    print("Type in: ")
    print("[ 1 ] to log in to you account")
    print("[ 2 ] to create a new account")
    print("[ 3 ] to exit the program")
    have_account = input("Type here: ")

    if have_account.upper() == "1":
        while True:
            user_name = input("\nEnter Username: ")
            password = input("Enter Password: ")
            if user_name == '111' and password == '111':
                # time.sleep(1)
                print("Login successful!")
                # time.sleep(1)
                main_menu()
            else:
                print("Password did not match!")
    elif have_account.upper() == "2":
        create_account()
    else:
        exit("Exiting Program...")


login()
