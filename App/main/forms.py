from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class FeedbackForm(FlaskForm):
    name = StringField(label='Username', validators=[DataRequired(), Length(min=2,max=30)])
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    subject = StringField(label='Subject', validators=[DataRequired(), Length(min=2,max=100)])
    message = TextAreaField(label='Message', validators=[DataRequired()])
    submit = SubmitField(label='Submit')
