# News API App


# Use the NewsAPI and the requests module to fetch the daily news related to different topics.
# Go to: https://newsapi.org/ and explore the various options to build you application


import requests
import json

query = input("What type of news you want to know????: ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-03-11&sortBy=publishedAt&apiKey=6f140bffe3de486bbda54eb8bb8184ba"
r = requests.get(url)

news = json.loads(r.text)
# print(news,type(news))

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("------------------------------------")
