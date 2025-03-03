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

print(response.text)

SHEETY_ENDPOINT = "https://api.sheety.co/14a00bdc0fae03aacc590eb008c2c254/workoutTracking/workouts"
sheety_header = {
    "Authorization" : "Basic SmFsYWwgQWJiYXNpOkoxMDY0ODg5OWEh"
}

today = datetime.now()
date = today.date()
time = today.time()
print(f"{date} \n {time}")
sheety_parameters = {
    "Date" : date.strftime("%d/%m/%Y"),
    "Time" : time.strftime("%-I:%M:%S %p"),
    "Exercise" : "",
    "Duration" : "",
    "Calories" : "",
}