import requests
import os


ENDPOINT = "https://www.nutritionix.com/v2/natural/exercise"

app_id = os.environ.get("NUTRITION_APP_ID ")
app_key = os.environ.get("NUTRITION_APP_API")

app_parameters = {
    "x-app-id" : app_id,
    "x-app-key" : app_key,
}