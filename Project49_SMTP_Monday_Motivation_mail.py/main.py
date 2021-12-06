
# SENDING A MOTIVATIONAL QUOTE VIA EMAIL USING PYTHON

import random
import datetime as dt
import smtplib

today =dt.datetime.now()
print(today)
Day = today.weekday()
print(Day)
#If weekday is Monday
if Day == 0:
    with open("quotes.txt") as file:
        contents = file.readlines()
        quote_to_be_sent = random.choice(contents)

    my_email="osrarts@gmail.com"
    pw = "*******"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=pw)
        connection.sendmail(from_addr=my_email, to_addrs="sro@gmail.com",msg=f"Subject:Monday Motivation\n\n{quote_to_be_sent}")
