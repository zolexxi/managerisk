from flask import Blueprint, render_template, request, make_response
from . import db
import pandas as pd
import numpy as np
from flask_login import login_required, current_user
import requests
from sqlalchemy import create_engine, Table, MetaData, select
import pymysql
from json2html import *

engine = create_engine('mysql+pymysql://asterisk:asterisk@192.168.0.106:3306/asterisk')
connection = engine.connect()

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


@main.route('/userbase')
@login_required
def userbase():
    from .models import ps_auths
    playerdetails = ps_auths.query.all()
    return render_template('userbase.html', name=current_user.name, playerdetails=playerdetails)

@main.route('/usermake', methods=['GET'])
@login_required
def usermake():
    return render_template('usermake.html')

@main.route('/usermake', methods=['POST'])
def usermake_get():
    from .models import ps_auths, ps_endpoints, ps_aors
    extension = request.form.get('extension')
    password = request.form.get('password')    
    id = request.form.get('extension')
    auth_type = 'userpass'
    transport = 'transport-udp'
    context = 'from-internal'
    disallow = 'all'
    allow = 'ulaw'
    direct_media = 'no'
    max_contacts = 1
    if extension and password:
        new_user = ps_auths(
            id=extension,
            password=password,
            auth_type=auth_type,
            username=extension
        ) 
        new_aor = ps_aors(
            id=extension,
            max_contacts=max_contacts
        )
        new_endpoint = ps_endpoints(
            id=extension,
            transport=transport,
            aors=extension,
            auth=extension,
            context=context,
            disallow=disallow,
            allow=allow,
            direct_media=direct_media
        )
    db.session.add(new_user)  # Adds new auth record to database
    db.session.add(new_aor)  # Adds new aor record to database
    db.session.add(new_endpoint)  # Adds new endpoint record to database
    db.session.commit()  # Commits all changes
    return make_response(f"{new_user} successfully created!")

@main.route('/userlist')
@login_required
def userlist():
    metadata = MetaData()
    extensions = Table('ps_auths', metadata, autoload=True, autoload_with=engine)
    stmt = select([extensions])
    results = connection.execute(stmt).fetchall()
    df = pd.DataFrame(results)
    df.columns = results[0].keys()
    dfhtml = df.to_html()
    return render_template('userlist.html', name='logins', ps_auths=dfhtml)

@main.route('/userstatus')
@login_required
def userstatus():
   resp = requests.get('http://192.168.0.106:8088/ari/endpoints?api_key=asterisk:asterisk')
   jresp = resp.json()
   return render_template('userstatus.html', jresp=jresp)

@main.route('/info')
@login_required
def info():
   resp = requests.get('http://192.168.0.106:8088/ari/asterisk/info?api_key=asterisk:asterisk')
   jresp = resp.json()
   hresp = json2html.convert(json = jresp)
   return render_template('info.html', hresp=json2html.convert(json = jresp))