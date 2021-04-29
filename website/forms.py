from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, InputRequired, Length, Email, EqualTo


class Register(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), InputRequired()])
    email = StringField('Email', validators=[
                        DataRequired(), Email(), InputRequired()])
    password1 = PasswordField(
        'Password', validators=[DataRequired(), InputRequired(), Length(min=7), EqualTo('password2', message='Passwords must match.')]
    )
    password2 = PasswordField(
        'Confirm Password', validators=[DataRequired(), InputRequired()]
    )


class Login(FlaskForm):
    email = StringField('Email', validators=[
                        DataRequired(), Email(), InputRequired()])
    password = PasswordField('Password', validators=[
                             DataRequired(), InputRequired()])
