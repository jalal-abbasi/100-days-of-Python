import requests
import os
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, body):
        self.api_key = "https://api.sheety.co/14a00bdc0fae03aacc590eb008c2c254/flightDeals/prices"
        self.body = body

    def edit_row(self, data):
        response = requests.put(url=self.api_key, json=data)
        response.raise_for_status()
        print(response.text)
