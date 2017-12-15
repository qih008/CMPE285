#CMPE285 HW2
#Qing Huang
#10/30/2017

from yahoo_finance import Share
#import quandl
import datetime

symbol = input('Please enter A stock symbol: ')

#mydata = quandl.get("WIKI/AAPL", rows=5)
stock = Share(symbol)

while stock.get_name() == None:
  print "you enter an invalid symbol or no network "
  symbol = input('Please enter A stock symbol: ')
  stock = Share(symbol)

now = datetime.datetime.now()

# cur_price = float(stock.get_price())
# open_price = float(stock.get_open())
# price_change = ""
# percentage_change = ""

# if cur_price > open_price:
#   price_change = cur_price - open_price
#   percentage_change = "(+{:.2%})".format(price_change/cur_price)
#   price_change = "+" + str(price_change)
# else:
#   price_change = open_price - cur_price
#   percentage_change = "(-{:.2%})".format(price_change/cur_price)
#   price_change = "-" + str(price_change)

print now
print stock.get_name(), "(" + symbol + ")"
#print cur_price, price_change, percentage_change
print stock.get_price(), stock.get_change(), stock.get_percent_change()