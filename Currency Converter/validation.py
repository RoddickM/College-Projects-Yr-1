def float_validation(text):
    while True:
        user_input = input(text)
        try:
            user_input = float(user_input)
            return user_input
        except ValueError:
            print("\n[ERROR!] Please only type in numbers!!!")


def range_validation(text, start_range, end_range):
    while True:
        try:
            user_input = int(input(text))
            if user_input in range(start_range, end_range+1):
                return str(user_input)
            else:
                print(f"\n[ERROR!] Please only enter numbers from {start_range} to {end_range}!!!")
        except ValueError:
            print("\n[ERROR!] Please only type in whole numbers!!!")


def y_or_n_validation(text):
    while True:
        user_input = input(text)
        if user_input in ["y", "Y", "n", "N"]:
            return user_input
        else:
            print("Please enter either Y or N in capitals or lowercase")
