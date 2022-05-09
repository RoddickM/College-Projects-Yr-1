import pandas as pd

import_data = pd.read_csv("dataset01.csv")


print(import_data.head())
print(import_data.head(12))
print(import_data.tail())
print(import_data.info())
