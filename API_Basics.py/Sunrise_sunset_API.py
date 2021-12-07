# request with parameters
import requests
import datetime as dt
# lets give parameters of our location
my_lat = 15.912900
my_long = 79.739990
parameters = {"lat": my_lat, "lng": my_long, "formatted": 0}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
print(response.status_code)
data = response.json()
print(data)
today=dt.datetime.now()
print(today)


##To check if exceptions are there (means not 200 code)
response.raise_for_status()