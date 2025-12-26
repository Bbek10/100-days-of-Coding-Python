import requests
import os
# from twilio.rest import Client // Uncomment this line if you want to use Twilio for SMS notifications

API_KEY = os.environ.API_KEY
# "YOUR_API_KEY"
# = API_KEY

MY_LAT = 27.717245
MY_LONG = 85.323959

N_LAT = 50.447731
N_LON = 30.542721

OWM_Endpoint = "http://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": N_LAT,
    "lon": N_LON,
    "appid": API_KEY,
    "cnt": 4,
}

r = requests.Session()
r = r.get(OWM_Endpoint, params=parameters)
weather_data = r.json()
weather_slice = weather_data["list"]    

will_rain = False


for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella today")