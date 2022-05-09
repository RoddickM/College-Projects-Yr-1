import pandas as pd

#stage 1
dataframe = pd.read_csv("baddata no.2.csv")
print(dataframe)

new_dataframe = dataframe.dropna()
print(new_dataframe.to_string())

dataframe.dropna(inplace=True)
print(dataframe.to_string())

dataframe.fillna(220, inplace=True)
print(dataframe.to_string())

dataframe["Calories"].fillna(129, inplace=True)
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

print("\n")

#stage 3
dataframe['Date'] = pd.to_datetime(dataframe['Date'])
print(dataframe.to_string())

dataframe['Date'] = pd.to_datetime(dataframe['Date'])
dataframe.dropna(subset=['Date'], inplace = True)
print(dataframe.to_string())

print("\n")

#stage4
dataframe.loc[7,'Duration'] = 45
print(dataframe.to_string())


for x in dataframe.index:
    if dataframe.loc[x, "Duration"] > 120:
        dataframe.loc[x, "Duration"] = 120

print(dataframe.to_string())


for x in dataframe.index:
    if dataframe.loc[x, "Duration"] > 120:
        dataframe.drop(x, inplace = True)

print(dataframe.to_string())

print("\n")

#stage 4
print(dataframe.duplicated())

dataframe.drop_duplicates(inplace = True)
print(dataframe.to_string())

