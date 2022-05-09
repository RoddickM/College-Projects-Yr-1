import pandas as pd

#stage 1
dataframe = pd.read_csv("baddata no.3.csv")
print(dataframe)

dataframe["Calories"].fillna(129, inplace=True)
print(dataframe.to_string())

dataframe.fillna(220, inplace=True)
print(dataframe.to_string())



print("\n")
#stage 2
x = dataframe["Calories"].mean()
dataframe["Calories"].fillna(x, inplace = True)
print(dataframe.to_string())

x = dataframe["Calories"].mode()[0]
dataframe["Calories"].fillna(x, inplace = True)
print(dataframe.to_string())

x = dataframe["Calories"].median()
dataframe["Calories"].fillna(x, inplace = True)
print(dataframe.to_string())