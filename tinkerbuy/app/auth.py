from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

# Create blueprint
auth = Blueprint('auth', __name__)

@auth.route('/auth')
def auth():
    return "TEST AUTH"



