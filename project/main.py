from flask import Blueprint, render_template, request, make_response
from . import db
from .models import ps_auths, ps_endpoints, ps_aors
import pandas as pd
import numpy as np
from flask_login import login_required, current_user
import requests
from sqlalchemy import create_engine, Table, MetaData, select
import pymysql
from json2html import json2html

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
    playerdetails = ps_auths.query.all()
    return render_template('userbase.html', name=current_user.name, playerdetails=playerdetails)

@main.route('/usermake', methods=['GET'])
@login_required
def usermake():
    return render_template('usermake.html')

@main.route('/usermake', methods=['POST'])
def usermake_get():
    extension = request.form.get('extension')
    password = request.form.get('password')    

    if not extension or not password:
        return make_response("Missing extension or password!", 400)

    auth_type = 'userpass'
    transport = 'transport-udp'
    context = 'from-internal'
    disallow = 'all'
    allow = 'ulaw'
    direct_media = 'no'
    max_contacts = 1

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

    db.session.add(new_user)
    db.session.add(new_aor)
    db.session.add(new_endpoint)
    db.session.commit()
    return make_response(f"{extension} successfully created!")

@main.route('/userlist')
@login_required
def userlist():
    df = pd.read_sql_table('ps_auths', con=db.engine)
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