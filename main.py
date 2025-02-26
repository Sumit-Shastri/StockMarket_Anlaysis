import pandas
import yfinance as yf

eicher = yf.Ticker("EICHERMOT.NS")
eicher_data = eicher.history(period="5y")
print(eicher_data.head())


