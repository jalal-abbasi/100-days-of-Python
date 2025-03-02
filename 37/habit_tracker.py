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
