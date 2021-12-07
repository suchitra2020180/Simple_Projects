# request without parameters
import requests
# RESPONSE TELLS US IF OUR REQUEST IS APPROVED OR NOT
response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response) # Here json format is expected
print(response.status_code)
# 1xx-Hold on; 2xx- Here is what you want ; 3xx- go away; 4xx- something wrong in server
if response.status_code != 200:
    raise Exception("Bad response from ISS API")

##To check if there are any exceptions
response.raise_for_status()

data =response.json()["iss_position"]

data = response.json()
longitude = data["iss_position"]["Longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude,longitude)
print(data)
print(iss_position)
