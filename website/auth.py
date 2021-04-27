from flask import Flask, Blueprint, render_template
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/')
def login():
    return render_template('base.html')


@auth.route('/logout')
def logout():
    return '<h1>Logout</h1>'


@auth.route('/sign_up')
def sign_up():
    return '<h1>Sign-up</h1>'
