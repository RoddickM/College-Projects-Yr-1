def int_validation(text):
    while True:
        try:
            user_input = int(input(text))
            return user_input
        except ValueError:
            print("\n[ERROR!] Please type in only whole numbers!!")


def int_range_validation(text, start_num, end_num):
    while True:
        user_input = int_validation(text)
        if user_input in range(start_num, end_num+1):
            return user_input
        else:
            print(f"[ERROR!] Please enter numbers between {start_num} and {end_num}")


def to_two_dp(number):
    return f"{number:.2f}"


def y_or_n_validation(text):
    while True:
        user_input = input(text)
        if user_input in ["Y", "N", "n", "y"]:
            return user_input
        else:
            print("[ERROR] Please only enter Y or N in upper or lower case")
