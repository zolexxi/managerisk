from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class ps_auths(db.Model):
    __tablename__ = 'ps_auths'

    id = db.Column(db.String(40), primary_key=True)
    password = db.Column(db.String(40))
    username = db.Column(db.String(40))
    auth_type = db.Column(db.String(40))

class ps_aors(db.Model):
    __tablename__ = 'ps_aors'

    id = db.Column(db.String(40), primary_key=True)
    max_contacts = db.Column(db.Integer())

class ps_endpoints(db.Model):
    __tablename__ = 'ps_endpoints'

    id = db.Column(db.String(40), primary_key=True)
    transport = db.Column(db.String(40))
    aors = db.Column(db.String(200))
    auth = db.Column(db.String(40))
    context = db.Column(db.String(40))
    disallow = db.Column(db.String(200))
    allow = db.Column(db.String(200))
    direct_media = db.Column(db.String(200))