from flask_wtf import Form
from wtforms import StringField, IntegerField, validators

class ethicalForm(Form):
    amount1 = IntegerField('amount1')

class growthForm(Form):
    amount2 = IntegerField('amount2')

class indexForm(Form):
    amount3 = IntegerField('amount3')

class qualityForm(Form):
    amount4 = IntegerField('amount4')

class valueForm(Form):
    amount5 = IntegerField('amount5')
