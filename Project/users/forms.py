from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, EqualTo, Email
from Project.models import User


class RegistrationForm(FlaskForm):
    username = StringField(label='Username', 
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField(label='Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField(label='Password',
                             validators=[DataRequired()])
    confirm_password = PasswordField(label='Confirm Your Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username was already taken. Please try a different name')
        
    def validate_email(self,email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Found another account with the same Email. Please try with a different Email ID')

class LoginForm(FlaskForm):
    email = StringField(label='Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField(label='Password',
                             validators=[DataRequired()])
    remember = BooleanField(label='Remember Me')
    submit= SubmitField(label='Login')


class UpdateAccountForm(FlaskForm):
    username= StringField(label='Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField(label='Email',
                        validators=[DataRequired(), Email()])
    picture = FileField(label='Update profile Picture', validators=[FileAllowed(['jpg','png','jpeg'])])
    submit= SubmitField(label='Update')

class RequestResetForm(FlaskForm):
    email = StringField(label='Email',
                        validators=[DataRequired(), Email()])
    submit= SubmitField(label='Request Password Reset')

    def validate_email(self,email):
        email = User.query.filter_by(email=email.data).first()
        if not email:
            raise ValidationError('There is no account with that email. You must register first.')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')

