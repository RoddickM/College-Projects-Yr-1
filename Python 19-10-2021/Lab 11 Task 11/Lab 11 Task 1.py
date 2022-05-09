import pandas as pd

import_data = pd.read_csv("Lab11.csv")

print(import_data)
import_data["Passed"] = import_data["Passed"].map({"yes": True, "no": False})
print(import_data)
