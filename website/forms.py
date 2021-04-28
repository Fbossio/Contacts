from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, InputRequired, Length, Email, EqualTo


class Register(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password1 = StringField('Password', validators=[
                            DataRequired(), Length(min=7), EqualTo('password2')])
    password2 = StringField('Confirm Password', validators=[DataRequired()])


class Login(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[DataRequired()])
