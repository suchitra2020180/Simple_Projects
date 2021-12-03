
import csv
with open("weather_data.csv") as file:
    data = csv.reader(file)  ##These are objects
    temperature = []
    for row in data:
        print(row)
        ##write all temperature values into a list
        t = row[1]
        if t != "temp":
            temperature.append(int(t))

print(f"Temperature: {temperature}")

import pandas as pd
c_data = pd.read_csv("weather_data.csv")
print(c_data.columns)
# converting data to dictionary
print(c_data.to_dict())
avg_temp = c_data["temp"].mean()
print(f"Avg_temp :{avg_temp}")

max_temp= c_data[c_data["temp"] == c_data["temp"].max()]
print(f"Max temp:", max_temp)

##Mondays temp in Fahrenheit

mon_temp_in_Celsius = c_data[c_data["day"]=="Monday"]["temp"]

temp_Fahrenheit = (int(mon_temp_in_Celsius) * (9/5)) +32
print(f"Temp of monday in Fahrenheit: {temp_Fahrenheit}")
