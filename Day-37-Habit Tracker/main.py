import requests

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

USER_TOKEN = "mowiewowiehawaii"
USER_NAME = "bbek10"
GRAPH_ID = "graph1"

user_params = {
    "token": USER_TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
#----user created
#response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
#print(response.text)

#----graph created
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Physiotherapy Graph",
    "unit": "minutes",
    "type": "float",
    "color": "ajisai"
}

#headers
headers = {
    "X-USER-TOKEN": USER_TOKEN
}
#response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
#print(response.text)

#----pixel created
from datetime import datetime
PIXELA_ENDPOINT = f"https://pixe.la/v1/users/{USER_NAME}/graphs/{GRAPH_ID}"

today = datetime.now()
custom_date = datetime(year=2026, month=1, day=26)
date = custom_date.strftime("%Y%m%d")

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    #"date": custom_date.strftime("%Y%m%d"),
    "quantity": "30",
}

#response = requests.post(url=PIXELA_ENDPOINT, json=pixel_data, headers=headers)
#print(response.text)

#--- Update a pixel in a graph i.e PUT request
GRAPH_PUT_ENDPOINT = f"{PIXELA_ENDPOINT}/{date}"

pixel_put_data = {
    "quantity": input("How many minutes did you do physiotherapy today? "),
}

#response = requests.put(url=GRAPH_PUT_ENDPOINT, json=pixel_data, headers=headers)
#print(response.text)

#--- Delete a pixel in a graph i.e DELETE request
GRAPH_DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{date}"
response = requests.delete(url=GRAPH_DELETE_ENDPOINT, headers=headers)
print(response.text)
