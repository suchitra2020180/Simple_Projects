# This is an Automated Birthday Wisher
# To run in cloud use pythonanywhere
import datetime as dt
import pandas as pd
import smtplib

my_email = "osrarts@gmail.com"
pw = "****"  # use your password

today = dt.datetime.now()
Birth_month = today.month
Birth_day = today.day
print(f"Month:{Birth_month}, Day:{Birth_day}")


data = pd.read_csv("Birthday_Dates.csv")
data.to_dict(orient="records")
print(data)
for (key, value) in data.iterrows():
    if value["Month"] == Birth_month:
        if value["Date_day"] == Birth_day:
            name = value["Name"]
            print(name)
            with open("Birthday_text.txt") as file:
                contents = file.read()
                new_content = contents.replace("[name]", name)
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=pw)
                #connection.sendmail(from_addr=my_email, to_addrs=value["Email"], msg=f"Subject: Birthday_Wisher\n\n Dear {name}: \n Happy Birthday")
                connection.sendmail(from_addr=my_email, to_addrs=value["Email"], msg=f"Subject: Birthday_Wisher\n\n {new_content}")

