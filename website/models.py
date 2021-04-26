from . import db
from flask_login import UserMixin


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.column(db.String(150), nullable=False)
    contacts = db.relationship('Contact', backref='users', lazy=True)

    def __repr__(self):
        return f'< User: {self.name} >'


class Contact(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(150))
    Type = db.Column(db.String(20), default='Other')
    user_id = db.Column(db.Integer, ForeignKey('users.id'))

    def __repr__(self):
        return f'< Contact: {self.email} >'
