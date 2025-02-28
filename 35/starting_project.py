import requests
from twilio.rest import Client


twilio_phone_number = "+18172413781"
account_sid = "Arr4512e"
auth_token = "1213"

api_key = "30b8331fb24765f13510612b4d8ae50e"
parameters = {
    "lat": 37.177338,
    "lon": -3.598557,
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
        body = "The weather will be shitty in the next 12 hours, bring your fucking umbrella!",
        from_ = twilio_phone_number,
        to = "+393428399994",
    )
    print(message.body)