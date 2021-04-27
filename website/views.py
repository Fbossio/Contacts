from flask import Flask, Blueprint

views = Blueprint('views', __name__)


@views.route('/contacts')
def contacts():
    return '<h1>Contacts</h1>'
