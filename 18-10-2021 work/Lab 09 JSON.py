import pandas as pd

import_data = pd.read_json("dataset02.js")


print(import_data.head())
print(import_data.head(12))
print(import_data.tail())
print(import_data.info())
