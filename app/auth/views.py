from flask import Blueprint, render_template
from flask_login import login_required
from app import app

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login')
def login():
    return render_template('auth/login.html')

@auth_bp.route('/protected')
@login_required
def protected():

    return render_template('auth/protected.html')

app = Flask(__name__, template_folder='app/templates')
