from flask_wtf import Form
from wtforms import StringField,SubmitField

class submitform(Form):
 querystring = StringField('Title')
 submit = SubmitField('Submit')