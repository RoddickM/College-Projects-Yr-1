from main import *

while True:
    user_name = input("Enter Username: ")
    password = input("Enter Password: ")
    if user_name == '111' and password == '111':
        time.sleep(1)
        print("Login successful!")
        time.sleep(1)
        main_menu()
    else:
        print("Password did not match!")