def int_validation(text):
    while True:
        try:
            user_input = int(input(text))
            return user_input
        except ValueError:
            print("[ERROR] Please only type in whole numbers in this field!!\n")


def int_range_check(text, min_value, max_value):
    while True:
        user_input = int_validation(text)
        if user_input in range(min_value, max_value+1):
            return user_input
        else:
            print(f"Please only type in a number between {min_value} and {max_value}!!\n")

