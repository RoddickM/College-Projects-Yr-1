import pandas as pd

import_data = pd.read_csv("Lab11.csv")

print(import_data)
print(import_data["Attempts"].sum())
