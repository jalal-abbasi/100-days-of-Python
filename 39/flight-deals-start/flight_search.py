import os
from logging import raiseExceptions
from os import environ

import requests
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.ACCESS_API = "https://test.api.amadeus.com/v1/security/oauth2/token"
        self.GET_API = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        self.ACCESS_PARAMS = {
            "grant_type" : "client_credentials",
            "client_id" : os.environ.get("AMADEUS_API_KEY"),
            "client_secret" : os.environ.get("AMADEUS_API_SECRET"),
        }
        self.ACCESS_HEADER = {"content-type" : "application/x-www-form-urlencoded"}
        try:
            self.TOKEN = os.environ.get("AMADEUS_TOKEN")
        except Exception:
            pass



    def request_access(self):
        response = requests.post(url=self.ACCESS_API, json=self.ACCESS_PARAMS, headers=self.ACCESS_HEADER)
        response.raise_for_status()
        print(response.status_code)
        os.environ["AMADEUS_TOKEN"]= response.json()["access_token"]

