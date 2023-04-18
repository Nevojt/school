import requests
from twilio.rest import Client


API_KEY = "431ed2e885ce6b4fb6475bf2713743dc"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
MY_LAT = 51.9264108
MY_LONG = 15.4800003

# Twilio
TWILIO_ACCOUNT_SID = "AC37953429152e6daa7dcea3f3aa247063"
TWILIO_AUTH_TOKEN = "e21689d29aa8382d3d70a31eec03fdad"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "units":"metric",
    "lang":"ua",
    "exclude": "current, minutely, daily"
}


response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()
weather_slice = data["list"][:12]

will_rain = False

for hour_data in weather_slice:
    weather = hour_data["weather"][0]["id"]
    if weather < 700:
        will_rain = True
        
if will_rain:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages \
                .create(
                     body="Візьми зонтик. Сьогодні буде дощ. ☂️",
                     from_='+19416771379',
                     to='+48534037393'
                 )
print(message.status)
