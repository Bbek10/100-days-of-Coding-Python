import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

r = requests.get(URL)
soup = BeautifulSoup(r.text, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

movies_titles = [movie.getText() for movie in all_movies]
movies_acending = movies_titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies_acending:
        file.write(f"{movie}\n")    
