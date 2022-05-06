import pandas as pd


# The menu() function generates the UI the accepts and validates user choice
def menu():

    flag = True

    while flag:
        print("######################################################")
        print("Which conversion would you like to make today?")
        print("1. Pound Sterling (GBP) to Euros (EUR)")
        print("2. Euros (EUR) to Pound Sterling(GBP)")
        print("3. Pound (GBP) to Australian Dollars (AUD)")
        print("4. Australian Dollars (AUD) to Pound Sterling (GBP)")
        print("5. Pound Sterling (GBP) to Japanese Yen (JPY)")
        print("6. Japanese Yen (JPY) to Pound Sterling (GBP)")
        print("7. Pound Sterling (GBP) to American Dollars (USD)")
        print("8. American Dollars (USD) to Pound Sterling (GBP)")
        print("")
        print("######################################################")
        
        convert_choice = input("Please enter the number of your choice (1-8): ")

        try:
            int(convert_choice)
        except TypeError:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(convert_choice) < 1 or int(convert_choice) > 8:
                print("Sorry, you did not neter a valid choice")
                flag = True
            else:
                return convert_choice


# Gets the short version of the conversion information based on user menu choice
def get_currency():
    currencies = {
       '1': 'GBP - EUR',
       '2': 'EUR - GBP', 
       '3': 'GBP - AUD',
       '4': 'AUD - GBP',
       '5': 'GPB - JPY',
       '6': 'JPY - GBP',
       '7': 'GBP - USD',
       '8': 'USD - GBP'}
   
    currency_to_convert = currencies.get(menu_choice)
    
    return currency_to_convert


menu_choice = menu()
currency = get_currency()


# The get_conversion_rate function uses pandas to get the latest conversion rate
# Imports a csv file in to a data frame
# Uses 'iloc' to get the last/most recent value in the selected column
def get_conversion_rate():
    df = pd.read_csv("Task4a_data.csv")
    
    current_conversion_rate = df[currency].iloc[-1]

    return current_conversion_rate


conversion_rate = get_conversion_rate()


# Accepts and validates user input for teh amount they want to convert
def get_amount_to_convert():
    print("You are converting: ", currency)
    
    flag = True
    
    while flag:
        amount_to_convert = input("please enter the amount you wish to convert")
    
        try:
            float(amount_to_convert)
        except TypeError:
            print("Sorry, you must enter a numerical value")
            flag = True
        else:
            return amount_to_convert


conversion_amount = float(get_amount_to_convert())


# Performs the conversion and outputs the final values
def perform_conversion():
    amount_received = round(conversion_amount * conversion_rate, 2)

    print("\n--------------------------------------------------------------------")
    print('You are converting {} in {}'.format(conversion_amount, currency[0:3]))
    print('You will receive {} in {}'.format(amount_received, currency[6:9]))


perform_conversion()
