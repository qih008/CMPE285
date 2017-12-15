from flask import render_template, request
from app import app
from .forms import profitForm

# index view function suppressed for brevity
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = profitForm()
    if request.method == 'POST':
        #proceeds = form.allotment.data
        symbol = form.symbol.data
        allotment = form.allotment.data
        final_price = form.final_price.data
        sell_commission = form.sell_commission.data
        init_price = form.init_price.data
        buy_commission = form.buy_commission.data
        tax_rate = form.tax_rate.data

        proceeds = allotment * final_price
        tax = tax_rate / 100.00 * (allotment * (final_price - init_price) - sell_commission - buy_commission)
        cost = allotment * init_price + sell_commission + buy_commission + tax
        break_price = (buy_commission + sell_commission) / float(allotment) + init_price

        s1 = "Proceeds: ${:,}".format(proceeds)
        s2 = "Cost: ${:,}".format(cost)
        s3 = "Cost details:"
        s4 = "Total purchasee price: ${:,}".format(allotment * init_price)
        s5 = "Buy commission: ${:,}".format(buy_commission)
        s6 = "Sell commission: ${:,}".format(sell_commission)
        s7 = "Tax on Captial Gain: {:,}%  of ${:,} = {:,}".format(tax_rate, (allotment * (final_price - init_price) - sell_commission - buy_commission), tax)
        s8 = "Net Profit: ${:,}".format(proceeds - cost)
        s9 = "Return on Investment: {:.2%}".format((proceeds - cost) / cost)
        s10 = "To break even, you should have a final share price of: ${:,}".format(break_price)

        return render_template('result.html', s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, s7=s7, s8=s8, s9=s9, s10=s10)
    return render_template('index.html', form=form)