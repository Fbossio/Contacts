from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
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


class UserContact(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), InputRequired()])
    email = StringField('Email', validators=[
                        DataRequired(), Email(), InputRequired()])
    phone = StringField('Phone', validators=[DataRequired(), InputRequired()])
    contact_type = SelectField('Type', choices=[(
        'Personal', 'Personal'), ('Profesional', 'Profesional'), ('Other', 'Other')])


class Search(FlaskForm):
    search = StringField('Search', validators=[DataRequired()])
