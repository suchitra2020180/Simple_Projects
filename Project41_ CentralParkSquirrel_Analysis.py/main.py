import pandas as pd
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#print(data.head())
#print(data.columns)
col = data["Primary Fur Color"].value_counts()
print(col)
new_data = pd.DataFrame(col, columns="Count")
print(new_data)
