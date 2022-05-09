# The function below validates whether the input field is empty or not
# The function uses an if-else statement
# The only parameter is the text that will be displayed to the user
def field_is_not_empty(text):
    while True:
        user_input = input(text)
        if len(user_input) > 0:
            return user_input
        else:
            print("\nPlease don't leave this field empty!!\n")


# The function below validates whether the input is a number
# The function uses a try-catch method
# The only parameter is the text that will be displayed to the user
def num_validation(text):
    while True:
        try:
            user_input = int(input(text))
            return user_input
        except ValueError:
            print("\nPlease enter a number!!\n")


# The function below validates the input only has letters and spaces
# The function uses an if-else statement
# The only parameter is the text that will be displayed to the user
def character_val(text):
    while True:
        user_input = field_is_not_empty(text)
        if all(x.isalpha() or x.isspace() for x in user_input):
            return user_input
        else:
            print("\nPlease enter only letters and spaces!!\n")


# The function below validates the input has less than 50 characters
# The function uses an if-else statement
# The only parameter is the text that will be displayed to the user
def length_validation(text):
    while True:
        user_input = character_val(text)
        if len(user_input) <= 50:
            return user_input
        else:
            print("\nPlease enter less than 50 characters!!\n")


# The function below validates the input entered is only "Y", "y", "N" or "n"
# The function uses an if-else statement
# The only parameter is the text that will be displayed to the user
def y_n_true_false(text):
    while True:
        user_input = input(text)
        if user_input == "N" or "n" or "y" or "Y":
            return user_input
        else:
            print("\nPlease only enter Y or N\n")
