from main import *


def login():
    while True:
        user_name = input("Enter Username: ")
        password = input("Enter Password: ")
        if user_name == '55' and password == '55':
            # time.sleep(1)
            print("\nLogin successful!\n")
            # time.sleep(1)
            main_menu()
        else:
            print("Password did not match!")


login()
