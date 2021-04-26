from flask import Flask, Blueprint

views = Blueprint('views', __name__)


@views.route('/contacts')
def contacts():
    pass
