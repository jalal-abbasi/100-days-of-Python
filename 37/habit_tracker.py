import requests
from datetime import datetime

create_user_url = "https://pixe.la/v1/users"
USERNAME = 'jalaladdin'
TOKEN = 'J10648899a!'
HEADERS = {
    "X-USER-TOKEN" : TOKEN,
}


create_user_data = {
    'token' : TOKEN ,
    'username' : USERNAME,
    'agreeTermsOfService' : 'yes',
    'notMinor' : 'yes'
}
requests.post(url=create_user_url, json=create_user_data)


create_graph_url = f"{create_user_url}/{USERNAME}/graphs"

create_graph_data = {
    'id' : 'codingtracker',
    'name' : 'Coding Tracker',
    'unit' : 'minute',
    'type' : 'int',
    'color' : 'sora',
}


response = requests.post(url=create_graph_url, json=create_graph_data, headers=HEADERS)
print(response.text)

