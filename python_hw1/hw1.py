#CMPE285 HW1
#Qing Huang
#10/24/2017

symbol = input('Please enter A stock symbol: ')
allotment = input('Please enter Allotment (number of shares): ')
final_price = input('Please enter Final share price (in dollars): ')
sell_commission = input('Please enter Sell commission (in dollars): ')
init_price = input('Please enter Inital share price (in dollars): ')
buy_commission = input('Please enter Buy commission (in dollars): ')
tax_rate = input('Please enter Captial gain tax rate (in %): ')

proceeds = allotment * final_price
tax = tax_rate / 100.00 * (allotment * (final_price - init_price) - sell_commission - buy_commission)
cost = allotment * init_price + sell_commission + buy_commission + tax
break_price = (buy_commission + sell_commission) / float(allotment) + init_price

print
print "PROFIT REPORT:"
print "Proceeds: ${:,}".format(proceeds)
print "Cost: ${:,}".format(cost)
print "Cost details:"
print "Total purchasee price:", allotment * init_price
print "Buy commission:", buy_commission
print "Sell commission:", sell_commission
print "Tax on Captial Gain: {:,}%  of ${:,} = {:,}".format(tax_rate, (allotment * (final_price - init_price) - sell_commission - buy_commission), tax)
print "Net Profit: ${:,}".format(proceeds - cost)
print "Return on Investment: {:.2%}".format((proceeds - cost) / cost)
print "To break even, you should have a final share price of: ${:,}".format(break_price)



