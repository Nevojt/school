import requests
from twilio.rest import Client


API_KEY = API
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
MY_LAT = 51.9264108
MY_LONG = 15.4800003

# Twilio
TWILIO_ACCOUNT_SID = "you SID"
TWILIO_AUTH_TOKEN = "you TOKEN"

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
                     from_='number TWILIO',
                     to='you number'
                 )
print(message.status)
