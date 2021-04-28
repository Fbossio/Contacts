from flask import Flask, Blueprint, render_template
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from .forms import Register, Login


auth = Blueprint('auth', __name__)


@auth.route('/')
def login():
    form = Login()
    return render_template('login.html', form=form)


@auth.route('/logout')
def logout():
    return '<h1>Logout</h1>'


@auth.route('/sign_up')
def sign_up():
    form = Register()
    return render_template('signup.html', form=form)
