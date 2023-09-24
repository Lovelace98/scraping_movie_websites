import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# This is a fun project i built to scrape the best hundred movies on the empire online website. Now I can get to enjoy all the top movies with my family without any hassle.

#This part of the code grabs the url link and then parse it using the html.parser
response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html5lib")

#This code gets all the movies in its html tags
all_movies = soup.find_all(name="h3", class_="title")

#This part gets the texts within those HTML tags
movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

#This saves all the movies in a .txt file
with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")


