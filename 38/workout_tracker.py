import requests
import os


ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

app_id = os.environ.get("NUTRITION_APP_ID")
app_key = os.environ.get("NUTRITION_APP_KEY")

headers = {
    "x-app-id" : app_id,
    "x-app-key" : app_key,
}

user_query = input("what exercise did you do today? ")
app_parameters = {
    "query" : user_query,
}

response = requests.post(url=ENDPOINT, json=app_parameters, headers=headers)

print(response.text)