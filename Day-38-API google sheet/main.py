import os
from dotenv import load_dotenv
load_dotenv()

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
SHEET_ENDPOINT = os.environ["SHEET_ENDPOINT"]


GENDER = "male"
WEIGHT_KG = 67
HEIGHT_CM = 175
AGE = 24    

BASE_URL = "https://app.100daysofpython.dev"
EXERCISE_ENDPOINT = f"{BASE_URL}/v1/nutrition/natural/exercise"




headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

import requests

post_data = {
    "query": input("Tell me which exercises you did today: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# exercise endpoint
# post to /v1/nutrition/natural/exercise
response = requests.post(url=f"{BASE_URL}/v1/nutrition/natural/exercise", json=post_data, headers=headers)
print(response.text)

result = response.json()

# add a new row to google sheet
import datetime 

today_date = datetime.datetime.now().strftime("%d/%m/%Y")
now_time = datetime.datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    

# Headers for authentication : Bearer Token

    bearer_headers = {
        "Authorization": f"Bearer {os.environ['BEARER_TOKEN']}"
    }
    # POST to google sheet
    sheet_response = requests.post(url=SHEET_ENDPOINT, json=sheet_inputs, headers=bearer_headers)
    print(sheet_response.text)


    #Remove hard coded API keys and tokens before sharing code
    # HINT 1: You'll need to import the os module.
    # HINT 2: Use the dotenv package to load the .env file and access the variables.
    # HINT 3: Use os.environ["<VARIABLE_NAME>"] to access the
    # variables you created in the .env file.
    
