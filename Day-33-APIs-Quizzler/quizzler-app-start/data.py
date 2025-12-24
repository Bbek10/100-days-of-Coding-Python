import requests
parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18,
}
r = requests.get("https://opentdb.com/api.php", params=parameters)
r.raise_for_status()
question_data = r.json()["results"]

#question_data = [
    
