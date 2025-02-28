import requests

api_key = "30b8331fb24765f13510612b4d8ae50e"
parameters = {
    "lat": 45.464203,
    "lon": 9.189982,
    "appid": api_key,
}
response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parameters)
response.raise_for_status()

data = response.json()
print(data)


