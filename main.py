import requests
from _datetime import datetime

USERNAME = "sophia34"
TOKEN = "ghjkghjkghjk3"
GRAPH_ID = "graph1"
PIXEL_ENDPOINT = "https://pixe.la/v1/users"
PIXEL_GRAPH_ENDPOINT = f"{PIXEL_ENDPOINT}/{USERNAME}/graphs"
PIXEL_POST_ENDPOINT = f"{PIXEL_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
PIXEL_UPDATE_ENDPOINT = f"{PIXEL_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/20210129"

user_params = {
    "token": USERNAME,
    "username": TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=PIXEL_ENDPOINT, json=user_params)
# print(response.text)

graph_config = {
    "id": GRAPH_ID,
    "name": "Walking Graph",
    "unit": "miles",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# graph_response = requests.post(url=PIXEL_GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(graph_response.text)

today = datetime.now()
pixel_post_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many miles did you walk today?"),
}

response = requests.post(url=PIXEL_POST_ENDPOINT, json=pixel_post_config, headers=headers)
print(response.text)

pixel_update_config = {
    "quantity": "3.5"
}

# response = requests.put(url=PIXEL_UPDATE_ENDPOINT, json=pixel_update_config, headers=headers)
# response = requests.delete(url=PIXEL_UPDATE_ENDPOINT, headers=headers)
# print(response.text)
