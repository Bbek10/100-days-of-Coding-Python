import os
import requests
from dotenv import load_dotenv

#load .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT ="https://api.sheety.co/e18cbf658bb96215ceb4dbcc02a4c58b/copyOfFlightDeals/prices"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._api_key = os.getenv("AMADEUS_API_KEY")
        self._api_secret = os.getenv("AMADEUS_API_SECRET")
        # Getting a new token every time program is run. Could reuse unexpired tokens as an extension.
        #self._token = self._get_new_token()
        self.destination_data = {}


    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data
        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)

    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers={
                    "Authorization": os.getenv("BEARER_TOKEN")
                }
            )
            return (response.text)

    


