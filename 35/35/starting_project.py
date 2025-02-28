import requests

api_key = "30b8331fb24765f13510612b4d8ae50e"
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
    print("the weather will be shitty in the next 12 hours, bring your fucking umbrella!")