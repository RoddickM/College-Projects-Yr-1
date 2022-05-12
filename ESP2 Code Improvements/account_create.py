import pandas as pd

accounts = {"username": [],
            "password": [],
            "permission": []}


def create_account():
    create_username = input("Create your username: ")
    create_password = input("Create your password: ")

    confirm_username = input("Confirm your username: ")
    confirm_password = input("Confirm your password: ")

    if create_username == confirm_username and create_password == confirm_password:
        print("Your account has been created!")


