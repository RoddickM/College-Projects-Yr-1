import pandas as pd

dataframe = pd.read_csv("baddata no.4.csv")
print(dataframe)

print("\n")
#stage 2
'''x = dataframe["Calories"].mean()
dataframe["Calories"].fillna(x, inplace = True)
print(dataframe.to_string())

x = dataframe["Calories"].mode()[0]
dataframe["Calories"].fillna(x, inplace = True)
print(dataframe.to_string())'''

x = dataframe["Calories"].median()
dataframe["Calories"].fillna(x, inplace = True)
print(dataframe.to_string())

