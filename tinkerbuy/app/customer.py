from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required
from app.blueprints import customer


# Customer dashboard route
@customer.route('/customer/dashboard')
#@login_required
def dashboard():
    #return render_template('customer/dashboard.html')
    return "<h1>CUSTOMER DASHBOARD</h1>"
