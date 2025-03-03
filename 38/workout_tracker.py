import requests
import os


ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

app_id = os.environ.get("NUTRITION_APP_ID")
app_key = os.environ.get("NUTRITION_APP_KEY")

headers = {
    "x-app-id" : app_id,
    "x-app-key" : app_key,
}

app_parameters = {
    "query" : "I ran three miles",
}

response = requests.post(url=ENDPOINT, json=app_parameters, headers=headers)

print(response.text)