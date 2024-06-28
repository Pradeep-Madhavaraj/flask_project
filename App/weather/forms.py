from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class WeatherForm(FlaskForm):
    city = StringField(label='City', validators=[DataRequired()])
    submit = SubmitField('Check')