import requests
from twilio.rest import Client
import os


twilio_phone_number = "+18172413781"
account_sid = "ACe34c895e1146f0a1b54f5e16d8c4512e"
auth_token = os.environ.get("AUTH_TOKEN")

api_key = os.environ.get("OWM_API_KEY")

parameters = {
    "lat": 45.463619,
    "lon": 9.188120,
    "appid": api_key,
    "cnt": 4,
}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

data = response.json()

will_rain = False
for timestep in data["list"]:
    if int(timestep["weather"][0]["id"]) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body = "The weather will be rainy in the next 12 hours, bring your umbrella!",
        from_ = twilio_phone_number,
        to = "+393428399994",
    )
    print(message.body)