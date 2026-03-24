import requests
from bs4 import BeautifulSoup


date = input("Which year do you want to travel to? Type the date in YYYY-MM-DD format: ")

url = "https://www.billboard.com/charts/hot-100/2000-08-12"

header = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.text, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

with open(f"songs {date}.txt", mode="w") as file:
    for song in song_names:
        file.write(f"{song}\n")