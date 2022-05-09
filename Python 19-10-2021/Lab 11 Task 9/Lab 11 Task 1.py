import pandas as pd

import_data = pd.read_csv("Lab11.csv")

print(import_data)
import_data.loc[10] = ["k", "Lydia", 12.4, 1, "yes"]
print(import_data)
