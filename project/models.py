from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class ps_auths(db.Model):
    id = db.Column(db.String(40), primary_key=True)
    password = db.Column(db.String(40))
    username = db.Column(db.String(40))