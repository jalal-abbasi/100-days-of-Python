import requests
import os
from datetime import datetime


NUTRITION_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutrition_app_id = os.environ.get("NUTRITION_APP_ID")
nutrition_app_key = os.environ.get("NUTRITION_APP_KEY")

headers = {
    "x-app-id" : nutrition_app_id,
    "x-app-key" : nutrition_app_key,
}

user_query = input("what exercise did you do today? ")
app_parameters = {
    "query" : user_query,
}

response = requests.post(url=NUTRITION_ENDPOINT, json=app_parameters, headers=headers)
data = response.json()
activity = data["exercises"][0]["name"]
duration = data["exercises"][0]["duration_min"]
nf_calories = data["exercises"][0]["nf_calories"]



os.environ["SHEETY_ENDPOINT"] = "https://api.sheety.co/14a00bdc0fae03aacc590eb008c2c254/workoutTracking/workouts"
sheety_endpoint = os.environ.get("SHEETY_ENDPOINT")

SHEETY_HEADER = {
    "Authorization" : os.environ.get("SHEETY_HEADER")
}

today = datetime.now()
date = today.date()
time = today.time()

sheety_parameters = {
    "workout" : {
            "date" : date.strftime("%d/%m/%Y"),
            "time" : time.strftime("%I:%M:%S %p").lstrip("0"),
            "exercise" : activity.title(),
            "duration" : duration,
            "calories" : nf_calories,
    }

}

sheety_response = requests.post(url=sheety_endpoint, json=sheety_parameters, headers=SHEETY_HEADER)
print(sheety_response.status_code)