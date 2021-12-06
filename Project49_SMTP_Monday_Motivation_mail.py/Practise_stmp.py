import smtplib
my_email = "osrarts@gmail.com"
password = "*******"

# Create object of smtplib as connection
#connection = smtplib.SMTP("smtp.gmail.com")

with smtplib.SMTP("smtp.gmail.com") as connection:
    # CONNECT TO TRANSPORT LAYER PROTOCOL
    connection.starttls()
    # login details
    connection.login(user=my_email, password=password)
    # GUEST DETAILS
    connection.sendmail(from_addr=my_email, to_addrs="sro@gmail.com", msg="Subject:Python\n\n This is done using python")
    #Close connection
    #connection.close()
