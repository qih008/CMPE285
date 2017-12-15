from flask_wtf import Form
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class profitForm(Form):
    symbol = StringField('symbol', validators=[DataRequired()])
    allotment = IntegerField('allotment')
    final_price = IntegerField('final_price')
    sell_commission = IntegerField('sell_commission')
    init_price = IntegerField('init_price')
    buy_commission = IntegerField('buy_commission')
    tax_rate = IntegerField('tax_rate')