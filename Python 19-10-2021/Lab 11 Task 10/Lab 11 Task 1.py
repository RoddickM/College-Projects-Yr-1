import pandas as pd

import_data = pd.read_csv("Lab11.csv")

print(import_data.to_string())

sorted_data = import_data.sort_values(by=["Name"], ascending=True)
print(sorted_data)


