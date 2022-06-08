import pandas as pd
import datetime
import matplotlib.pyplot as plt

df = pd.read_csv("Task_4a_data.csv")

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
    return df_search


date_list = ind_emp_check(df, "201111", s_date, e_date)
date_list = date_list["index"].values.tolist()

list_of_numbers = {}

for i in date_list:
    region = df[[i]].loc[df["Region"] == "London"]

    num = 0
    for a in range(len(region)):
        num += region.iloc[a]
    list_of_numbers[i] = int(num)

names = list(list_of_numbers.keys())
values = list(list_of_numbers.values())

plt.bar(names, values)
plt.xticks(rotation=90)
plt.show()
