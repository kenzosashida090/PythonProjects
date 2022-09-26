from bs4 import BeautifulSoup

import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpages = response.text

soup = BeautifulSoup(yc_webpages, "html.parser")

article_tag = soup.find_all(class_="titlelink")
article_texts = []
article_links = []
article_scores = []
for i in article_tag:
    text = i.getText()
    article_texts.append(text)
    article_link = i.get("href")
    article_links.append(article_link)

article_upbvote = [ int(score.getText().split()[0])  for score in soup.find_all(name="span", class_ = "score")]

# print(article_texts)
# print(article_links)

max_score = max(article_upbvote)
a_string = soup.find(string=f"{max_score} points")

index = article_upbvote.index(max_score)
print(article_links[index])
print(article_texts[index])




# for score in soup.find_all(name="span", class_ = "score"):
#   if score.getText() == f"{max_score} points" :
#      print( score.findParent("a"))


# print(type(f"{max_score} points"))
# for i in article_upbvote:
#     if i == max_score:
#         print(i)

# for i in article_upbvote:
#    x= int( i.split()[0] )
#    print(type(x))












# import lxml
# with open("website.html",encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
#
# # print(soup.title)
#
# all_paragraphs = soup.find_all(name = "a")
#
# for i in all_paragraphs:
#     # print(i.getText())
#     print(i.get("href"))
#
# heading = soup.find("h1", id = "name")
# section_heading = soup.find("h3", class_= "heading")
# print(heading)
# print(section_heading.get("class"))
#
# name = soup.select_one(selector="#name") # for an id
# print(name)
#
# headings = soup.select(".heading") # will create a list that contains all the selected classes
# print(headings)