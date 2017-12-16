import quandl
import pandas as pd
import datetime
from datetime import timedelta


quandl.ApiConfig.api_key = "E1yyuR2R1ip6VeYjkfWn"

mydata = quandl.get("WIKI/MSFT", rows=5)
price_list = []
time_list = []
now = datetime.date.today()

for i in range(5):
  close_price = float(mydata['Close'][i])
  price_list.append(close_price)
  t = now - timedelta(days=(4-i))
  time_list.append(t.strftime('%m-%d-%Y'))




print price_list
print time_list
