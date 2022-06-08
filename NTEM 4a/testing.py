import pandas as pd
import datetime

df = pd.read_csv("Task_4a_data.csv")

staff_id = int(input("Enter the Employee Id : "))
s_date = input("Enter Starting Date in dd/mm/yyyy: ")
day, month, year = s_date.split("/")
s_date = datetime.date(int(year), int(month), int(day))
e_date = input("Enter End Date in dd/mm/yyyy: ")
day, month, year = e_date.split("/")
e_date = datetime.date(int(year), int(month), int(day))
s_date = datetime.datetime.strptime(s_date.strftime('%d/%m/%Y'), '%d/%m/%Y')
e_date = datetime.datetime.strptime(e_date.strftime('%d/%m/%Y'), '%d/%m/%Y')


def ind_emp_check(df_r, staff_idd, start_date, end_date):
    df_r = df_r.loc[df.index == staff_idd]

    df_r = df_r.T[4:]
    df_r.reset_index(inplace=True)
    df_r['ID1'] = pd.to_datetime(df_r['index'], format='%d/%m/%Y')
    start_date = pd.to_datetime(start_date, format='%d/%m/%Y')
    end_date = pd.to_datetime(end_date, format='%d/%m/%Y')
    mask = (df_r['ID1'] >= start_date) & (df_r['ID1'] <= end_date)
    df_search = df_r.loc[mask]
    list(df_search)
    print(df_search)


'''region = df[["15/01/2021"]].loc[df["Region"] == "London"]
list_of_numbers = {}


num = 0
for i in range(len(region)):
    num += region.iloc[i]
    print(int(num))
list_of_numbers["15/01/2021"] = int(num)
print(list_of_numbers)'''

ind_emp_check(df, "201111", s_date, e_date)

