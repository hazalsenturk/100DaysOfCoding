import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"

response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, "html.parser")

movie_titles = soup.find_all(name="td", class_="titleColumn")

movie_list = []

for movie in movie_titles:
    name = movie.getText()
    movie_list.append(name)

new_list = []

with open("movies.txt", "a") as file:
    for element in movie_list:
        element = element.split("\n")
        label = str(f"{element[1]} {element[2]} {element[3]}\n")
        label = label.replace("   " , "")
        new_list.append(label)
        file.write(label)

with open("movies.txt") as file:
    content = file.read()



