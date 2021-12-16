# https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
# Place the code in pythonanywhere to run daily at 7:00am
import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
Twilio_id = "##"
Twilio_API_key="key"
API_key = "Your VIRTU_API"
param = {
            "lat": 23.610182,
            "lon": 85.279938,
            "appid":API_key,
            "exclude": "current,minutely,daily"
            }
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=param)
response.raise_for_status()
data = response.json()
print(data)
hourly_list =data['hourly']
print("Hourly list:", hourly_list)
print("Length of Hourly list:", len(hourly_list))
# for item, value in data.items():
#     key = item
#     #print(key)
#     #print(value)
#     if key=="hourly":
#         hourly_list = value
#         print("Hourly list:", hourly_list)
#         print("Length of Hourly list:", len(hourly_list))
weather_data=[]
weather_slicer=hourly_list[20:]
print("Weather slicer:", weather_slicer)
print("Length of Weather slicer:", len(weather_slicer))
for i in range(0, len(weather_slicer)):
    ID =weather_slicer[i]['weather'][0]["id"]
    print(ID)
    if ID > 800:
        will_rain = True

if will_rain:
    print("Bring Umbrella")
    # when using twilio free account to send messages
    proxy_client=TwilioHttpClient()
    proxy_client.session.proxies ={'https':os.environ['https_proxy']}
    client = Client(Twilio_id, Twilio_API_key,proxy_client)
    message = client.messages \
        .create(
        body="It may rain today .Please take umbrella",
        from="twilio generated phone num",
        to="Sender phone number"
    )
    print(message.status)


#
# for hour in range(0, 12):
#     for i in hourly_list:   # only 12 items from hourly_list==> means 12 hour data
#         for key, value in i.items():
#             if key == "weather":
#                 w_data = {key:value}
#                 weather_data.append(w_data)
# print("======weather data======")
# print(weather_data)
#     #if item[0]=="hourly":
#         #print(item)

# hour_data =[value for item,value in data.items() if item == "hourly"]
# print("Hour Data:", hour_data)
# print("Length of hourly data", len(hour_data))
# for i in hour_data:
#     print(i)