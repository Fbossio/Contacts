from flask import Flask, Blueprint
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/')
def login():
    pass


@auth.route('/logout')
def logout():
    pass


@auth.route('/sign_up')
def sign_up():
    pass
