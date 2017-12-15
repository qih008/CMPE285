import quandl
import pandas as pd

quandl.ApiConfig.api_key = "E1yyuR2R1ip6VeYjkfWn"

df = pd.read_csv('secwiki_tickers.csv')

symbol = input('Please enter A stock symbol: ')

mydata = quandl.get("WIKI/"+symbol)

print mydata
# test = df[df.Ticker==symbol]
# if not test.Name.values:
#   print("List is empty")