import pandas as pd

import_data = pd.read_csv("Lab11.csv")

print(import_data.to_string())
print(import_data.head(3))
