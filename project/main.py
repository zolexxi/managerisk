from flask import Blueprint, render_template, request, make_response
from . import db
import pandas as pd
import numpy as np
from flask_login import login_required, current_user

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
