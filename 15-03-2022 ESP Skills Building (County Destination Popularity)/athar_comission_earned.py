import pandas as pd

df = pd.read_csv("EstateAgents.csv")

commission_date = "January"

extract_comm = df.loc[(df["Estate Agent"] == "Athar Estates"), df.columns != "Estate Agent"]
extract_comm["Commission Earned"] = round(extract_comm["Consultation fees"] * (extract_comm["Commission (%)"] / 100), 2)

comm_calculated = extract_comm.to_string(index=False)

total_commission = round(extract_comm["Commission Earned"].sum(), 2)

print("Here is a breakdown of the comission earned in for Athar Estates")
print(comm_calculated)
print(f"The total comission earned in all year for Athar Estate was £{total_commission}")


df = pd.read_csv("EstateAgents.csv")

commission_date = "January"

extract_comm = df.loc[(df["Month"] == "January"), df.columns != "Month"]
extract_comm["Commission Earned"] = round(extract_comm["Consultation fees"] * (extract_comm["Commission (%)"] / 100), 2)

comm_calculated = extract_comm.to_string(index=False)

total_commission = round(extract_comm["Commission Earned"].sum(), 2)

print(f"Here is a breakdown of the comission earned in {commission_date}")
print(comm_calculated)
print(f"The total comission earned in {commission_date} was £{total_commission}")
