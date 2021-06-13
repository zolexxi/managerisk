from flask import Blueprint, render_template
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


@main.route('/userbase', methods=("POST", "GET"))
@login_required
def userbase():
    return render_template('userbase.html')