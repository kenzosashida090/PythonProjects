import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
top_movies = response.text
soup = BeautifulSoup(top_movies,"html.parser")


top = soup.find_all("h3",class_="title") # doesent creat a list 
with open("movies.txt",'w',encoding="utf8") as file:
    for i in top[::-1]:
        movies=i.getText()
        contents = file.write(f"{movies}\n")
# new_list = i.getText() for i in top[::-1]


# class slice(start,stop,[step] to inverse de list order

