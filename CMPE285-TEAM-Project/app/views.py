from flask import render_template, request
from app import app
from .forms import ethicalForm, growthForm, indexForm, qualityForm, valueForm

import quandl
import datetime
import pandas as pd

# index view function suppressed for brevity
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    ethical_form = ethicalForm()
    growth_form = growthForm()
    index_form = indexForm()
    quality_form = qualityForm()
    value_form = valueForm()

    if request.method == 'POST':
        
        if ethical_form.amount1.data is not None:
            amount = ethical_form.amount1.data
            a1 = "The investment amount is: ${:,}".format(amount)
            title1 = "Ethical Investing Method"
            stock1 = "AAPL 50%"
            stock2 = "ADBE 30%"
            stock3 = "NSRGY 20%"
            return render_template('ethical.html', s1=a1, title=title1, s2=stock1, s3=stock2, s4=stock3)
        elif growth_form.amount2.data is not None:
            amount = growth_form.amount2.data
            a1 = "The investment amount is: ${:,}".format(amount)
            title1 = "Growth Investing Method"
            stock1 = "TSLA 50%"
            stock2 = "INTC 25%"
            stock3 = "AMZN 25%"
        elif index_form.amount3.data is not None:
            amount = index_form.amount3.data
            a1 = "The investment amount is: ${:,}".format(amount)
            title1 = "Index Investing Method"
            stock1 = "VTI 33%"
            stock2 = "IXUS 33%"
            stock3 = "ILTB 33%"
        elif quality_form.amount4.data is not None:
            amount = quality_form.amount4.data
            a1 = "The investment amount is: ${:,}".format(amount)
            title1 = "Quality Investing Method"
            stock1 = "FB 50%"
            stock2 = "MSFT 20%"
            stock3 = "SNE 30%"
        elif value_form.amount5.data is not None:
            amount = value_form.amount5.data
            a1 = "The investment amount is: ${:,}".format(amount)
            title1 = "Value Investing Method"
            stock1 = "NFLX 80%"
            stock2 = "TWTR 15%"
            stock3 = "GOOGL 5%"
        


        return render_template('result.html', s1=a1, title=title1, s2=stock1, s3=stock2, s4=stock3)
    return render_template('index.html', ethical_form=ethical_form, growth_form=growth_form, index_form=index_form, quality_form=quality_form, value_form=value_form)




