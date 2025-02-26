import pandas
import yfinance as yf
from newsapi import NewsApiClient

#Eicher data fetching
eicher = yf.Ticker("EICHERMOT.NS")
eicher_data = eicher.history(period="5y")
print(eicher_data.head())

#News fetching
newsapi = NewsApiClient(api_key="f1b9b05102bc4fee9fb107ce42f4cd14")
articles = newsapi.get_everything(q="Eicher Motors", language="en", sort_by="publishedAt")

# Display top 5 news headlines
for article in articles["articles"][:5]:
    print(article["title"], "-", article["url"])





