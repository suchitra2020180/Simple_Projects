# Sending  motivational_quote via email on current weekday using python
# For sending email through python we need to lower the security of gmail

# ------------------------datetime module ---------------------

import datetime as dt
today = dt.datetime.now()
Year = today.year
print(Year)
Month = today.month
Day = today.weekday()
print(Day)

#----------------------Reading motivational quotes---------------
import random
with open("quotes.txt") as file:
    contents = file.readlines()
    print(random.choice(contents))
    quote_to_be_sent = random.choice(contents)


# ----------------------------------SMTP module------------------
import smtplib
my_email = "osrarts@gmail.com"
password = "******"

with smtplib.SMTP("smtp.gmail.com") as connection:
    # CONNECT TO TRANSPORT LAYER PROTOCOL
    connection.starttls()
    # login details
    connection.login(user=my_email, password=password)
    # GUEST DETAILS
    connection.sendmail(
        from_addr=my_email,
        to_addrs="sro@gmail.com",
        msg=f"Subject:Monday Motivation\n\n{quote_to_be_sent}")

