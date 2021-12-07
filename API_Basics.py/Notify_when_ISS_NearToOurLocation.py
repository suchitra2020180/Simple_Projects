# Sending a mail when the iss is near to our position and at night
import requests
import smtplib
import datetime as dt
import time
today = dt.datetime.now()
print(today)
my_hour =today.hour
print("MY HOUR:", my_hour)
my_mail="osrarts@gmail.com"
pw="$uch!tr@"
response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.status_code)
response.raise_for_status()
my_lat = 15.912900
my_long = 79.739990

data = response.json()
print(data)
print(data['iss_position'])
iss_lat = float(data['iss_position']['latitude'])
print(iss_lat)
iss_long = float(data['iss_position']['longitude'])
print(f"iss_lat:{iss_lat}, iss_long:{iss_long}")
print(f"my_lat:{my_lat}, my_long:{my_long}")
iss_location=(iss_lat, iss_long)
parameters = {"lat": my_lat, "lng": my_long, "formatted": 0}

##-------------------------For night time
sun_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
print(sun_response.status_code)
sun_data = sun_response.json()
print("sun_data:", sun_data)
sun_set = sun_data['results']['sunset']
sun_set_hour = int(sun_data['results']['sunset'].split('T')[1].split(':')[0])
print("sun_set:", sun_set)
print("sun_set_HOUR:", sun_set_hour)
sun_rise_hour = int(sun_data['results']['sunrise'].split('T')[1].split(':')[0])
print("sun_rise_HOUR:", sun_rise_hour)


lat_ad = iss_lat + 5
lat_ba = iss_lat - 5
long_ad = iss_long + 5
long_ba = iss_long - 5
while True:
    time.sleep(60)
    if lat_ba <= iss_lat <= lat_ad and long_ba <= iss_long <= long_ad:
        if my_hour >= sun_set_hour or my_hour <= sun_rise_hour:
            print("Match found")
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_mail, password=pw)
                connection.sendmail(from_addr=my_mail, to_addrs="suchitraraniojha@gmail.com", msg= "Subject:ISS position\n\n Look up")
        print("End of the code")