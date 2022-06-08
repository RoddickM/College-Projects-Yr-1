import datetime
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime as dt

df = pd.read_csv('Task_4a_data.csv', index_col='ID')


def main_menu():
    menu_display = "Welcome to NTEM sales Dashboard"
    menu_display += "\nPlease type the number next to the action you desire"
    menu_display += "\n> [ 1 ] Enter sales record"
    menu_display += "\n> [ 2 ] Run reports"
    menu_display += "\n> [ 3 ] Exit"
    print(menu_display)
    user_input = int(input("Type the number here: "))
    return user_input


def ind_emp_check(df_r, staff_id, date1, date2):
    df_r = df_r.loc[df.index == staff_id]

    df_r = df_r.T[3:]
    df_r.reset_index(inplace=True)
    df_r['ID1'] = pd.to_datetime(df_r['index'], format='%d/%m/%Y')
    date1 = pd.to_datetime(date1, format='%d/%m/%Y')
    date2 = pd.to_datetime(date2, format='%d/%m/%Y')
    mask = (df_r['ID1'] >= date1) & (df_r['ID1'] <= date2)
    df_search = df_r.loc[mask]
    print(df_search)
    print('Total by id = {} is £{}.00'.format(staff_id, sum(df_search[staff_id])))

    plt.bar(df_search['index'], df_search[staff_id])
    plt.xticks(rotation=90)
    plt.show()


def sales_record():
    staff_id = int(input("Enter the Staff ID "))
    if staff_id not in df.index.values:
        print('yes')

    date1 = input("Enter Date in dd/mm/yy: ")
    day, month, year = date1.split("/")
    date1 = datetime.date(int(year), int(month), int(day))

    if datetime.datetime.strptime(date1.strftime('%d/%m/%Y'), '%d/%m/%Y') > datetime.datetime.strptime(
            dt.today().strftime('%d/%m/%Y'), '%d/%m/%Y'):
        print("Date is in the future")
    else:
        cost = float(input("Enter the cost : "))
        df.loc[staff_id, date1.strftime('%d/%m/%Y')] = cost


def run_reports():
    staff_id = int(input("Enter the Employee Id : "))
    s_date = input("Enter Starting Date in dd/mm/yyyy: ")
    day, month, year = s_date.split("/")
    s_date = datetime.date(int(year), int(month), int(day))

    e_date = input("Enter End Date in dd/mm/yyyy: ")
    day, month, year = e_date.split("/")
    e_date = datetime.date(int(year), int(month), int(day))

    s_date = datetime.datetime.strptime(s_date.strftime('%d/%m/%Y'), '%d/%m/%Y')
    e_date = datetime.datetime.strptime(e_date.strftime('%d/%m/%Y'), '%d/%m/%Y')
    ind_emp_check(df, staff_id, s_date, e_date)
    print("")  # adds an empty line


def sales_dashboard():
    while True:
        menu_choice = main_menu()
        if menu_choice == 1:
            sales_record()
        elif menu_choice == 2:
            run_reports()
        else:
            exit("BYE BYE!")


sales_dashboard()
