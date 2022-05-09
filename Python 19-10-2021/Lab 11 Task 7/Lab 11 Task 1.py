import pandas as pd

import_data = pd.read_csv("Lab11.csv")

print(import_data.to_string())
import_data.loc[3, "Result"] = 10.4
print(import_data.to_string())
