import re


def length_validation(text=None, length_needed=None):
    while True:
        user_input = input(text)
        if len(user_input) <= length_needed:
            if any(char.isdigit() for char in user_input):
                print(f"Don't enter numbers when typing!!")
            else:
                return user_input
        else:
            print(f"\nPlease enter less than {length_needed} character(spaces are included).\n")


def has_character(text=None, has=None):
    while True:
        user_input = input(text)
        if has in user_input:
            return user_input
        else:
            print(f"\nPlease enter the {has} symbol.\n")


def post_code_validation(text=None):
    while True:
        user_input = input(text)
        if re.match("^[a-zA-Z][0-9]{3}[a-zA-Z]{2}$", user_input):
            return user_input
        elif re.match("^[a-zA-Z]{2}[0-9]{2}[a-zA-Z]{2}$", user_input):
            return user_input
        elif re.match("^[a-zA-Z]{2}[0-9]{3}[a-zA-Z]{2}$", user_input):
            return user_input
        else:
            print("Please enter the postcode in the right format")


def date_validation(text=None):
    while True:
        user_input = input(text)
        if re.match("^[0-9]{2}/[0-9]{2}/[0-9]{4}$", user_input):
            return user_input
        else:
            print("Please enter your the of birth in the DD/MM/YYYY format")


def age_validation(text=None, age_start=None, age_end=None):
    while True:
        try:
            user_input = int(input(text))
            if user_input in range(age_start, age_end):
                return user_input
            else:
                print(f"Please enter a number between {age_start} {age_end-1}")
        except ValueError:
            print("Please enter a number!")


def check(text=None):
    while True:
        user_input = input(text)
        if re.match('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', user_input):
            print("Valid Email")
        else:
            print("Invalid Email")
