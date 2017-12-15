#CMPE285 HW2
#Qing Huang
#11/05/2017

import quandl
import datetime
import pandas as pd

quandl.ApiConfig.api_key = "E1yyuR2R1ip6VeYjkfWn"
df = pd.read_csv('secwiki_tickers.csv')

symbol = input('Please enter A stock symbol: ')

stock_name = df[df.Ticker==symbol]

while not stock_name.Name.values:
  print "you enter an invalid symbol or no network "
  symbol = input('Please enter A stock symbol: ')
  stock_name = df[df.Ticker==symbol]


mydata = quandl.get("WIKI/"+symbol, rows=1)
now = datetime.datetime.now()

close_price = float(mydata['Close'])
open_price = float(mydata['Open'])
price_change = ""
percentage_change = ""

if close_price > open_price:
  price_change = close_price - open_price
  percentage_change = "(+{:.2%})".format(price_change/open_price)
  price_change = "+" + str(price_change)
else:
  price_change = open_price - close_price
  percentage_change = "(-{:.2%})".format(price_change/open_price)
  price_change = "-" + str(price_change)

print now
print stock_name.Name.values[0], "(" + symbol + ")"
print close_price, price_change, percentage_change
#print stock.get_price(), stock.get_change(), stock.get_percent_change()