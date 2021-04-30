from flask import Flask, Blueprint, render_template
from flask_login import login_required, current_user
from .forms import UserContact
from .models import Contact
from . import db
from .helpers import flash_errors


views = Blueprint('views', __name__)


@views.route('/contacts')
def contacts():
    form = UserContact()
    return render_template('contacts.html', form=form, user=current_user)
