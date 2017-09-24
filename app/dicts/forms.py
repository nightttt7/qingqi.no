from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class dictsForm(FlaskForm):
    englishword = StringField('english word', validators=[Required()])
    submit1 = SubmitField('translate')