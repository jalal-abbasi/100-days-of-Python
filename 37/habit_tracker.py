import requests
from datetime import datetime

create_user_url = "https://pixe.la/v1/users"
USERNAME = 'jalaladdin'
TOKEN = 'J10648899a!'
HEADERS = {
    "X-USER-TOKEN" : TOKEN,
}
#
#
# create_user_data = {
#     'token' : TOKEN ,
#     'username' : USERNAME,
#     'agreeTermsOfService' : 'yes',
#     'notMinor' : 'yes'
# }
# requests.post(url=create_user_url, json=create_user_data)
#
#
create_graph_url = f"{create_user_url}/{USERNAME}/graphs"
#
# create_graph_data = {
#     'id' : 'codingtracker',
#     'name' : 'Coding Tracker',
#     'unit' : 'minute',
#     'type' : 'int',
#     'color' : 'sora',
# }
#
#
# requests.post(url=create_graph_url, json=create_graph_data, headers=HEADERS)


today = datetime.now()
yesterday = datetime(year=2025, month=3, day=1)
create_pixel_url = f"{create_graph_url}/codingtracker"
# create_pixel_data = {
#     'date' : yesterday.strftime("%Y%m%d"),
#     'quantity' : '200',
# }
#
# requests.post(url=create_pixel_url, json=create_pixel_data, headers=HEADERS)

update_pixel_url = f"{create_pixel_url}/{yesterday.strftime("%Y%m%d")}"

update_pixel_data = {
    'quantity' : '220'
}

response = requests.put(url=update_pixel_url, json=update_pixel_data, headers=HEADERS)
print(response.text)