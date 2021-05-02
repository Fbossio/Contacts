from flask import Flask, Blueprint, render_template, flash, request, jsonify
from flask_login import login_required, current_user
from .forms import UserContact, Search
from .models import Contact
from . import db
from .helpers import flash_errors


views = Blueprint('views', __name__)


@views.route('/contacts', methods=['GET', 'POST'])
@login_required
def contacts():
    form = UserContact()
    if request.method == 'POST':
        if form.validate():
            request_data = request.get_json()
            name = request_data['name']
            email = request_data['email']
            phone = request_data['phone']
            Type = request_data['Type']

            try:
                new_contact = Contact(
                    name=name, email=email, phone=phone, Type=Type, user_id=current_user.id)
                db.session.add(new_contact)
                db.session.commit()
            except AssertionError as error:
                flash(error, category='error')
                db.session.rollback()
    return render_template('contacts.html', form=form, user=current_user, data=Contact.query.filter_by(user_id=current_user.id).order_by('id').all())


@views.route('/delete_contact/<contactId>', methods=['DELETE'])
@login_required
def delete_contact(contactId):
    contact = Contact.query.get(contactId)
    if contact:
        try:
            db.session.delete(contact)
            db.session.commit()
        except AssertionError as error:
            flash(error, category='error')
            db.session.rollback()
    return jsonify({})
