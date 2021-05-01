from flask import Flask, Blueprint, render_template
from flask_login import login_required, current_user
from .forms import UserContact, Search
from .models import Contact
from . import db
from .helpers import flash_errors


views = Blueprint('views', __name__)


@views.route('/contacts')
def contacts():
    form = UserContact()
    searchForm = Search()
    return render_template('contacts.html', form=form, searchForm=searchForm, user=current_user)
