import pandas as pd

import_data = pd.read_csv("Lab11.csv")

print(import_data.to_string())

for i in import_data.index:
    passed = import_data["Attempts"][i]
    if passed > 2:
        print(import_data.loc[i])


