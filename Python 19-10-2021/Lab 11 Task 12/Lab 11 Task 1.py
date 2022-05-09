import pandas as pd

import_data = pd.read_csv("Lab11.csv")

print(import_data)
import_data.pop("Attempts")
print(import_data)
