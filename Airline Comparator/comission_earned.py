import pandas as pd

df = pd.read_csv("Task4a_data 1.csv")


def view_raw_comission_data():
    commission_data = df[["Price", "Commission (%)"]]

    price = commission_data["Price"]
    commission = commission_data["Commission (%)"]

    comission_earned = []

    print("Here is the raw data for all the comission earned by each airline")
    print("It is ordered by the index from the original file")

    for i in price.index:
        total_comission_earned = price[i] * (commission[i] / 100)
        comission_earned.append(round(total_comission_earned, 2))

    df["Comission Earned (£)"] = comission_earned

    extract = df.loc[(df['Month'] == "January") & (df['Airline'] == "Yorkshire Airlines"), (df.columns != "Month") & (df.columns != "Destination")]
    print(extract.to_string(index=False))



