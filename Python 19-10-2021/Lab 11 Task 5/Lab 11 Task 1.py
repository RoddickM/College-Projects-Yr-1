import pandas as pd

import_data = pd.read_csv("Lab11.csv", usecols=["Name", "Result"], low_memory=True)

print(import_data.to_string())
