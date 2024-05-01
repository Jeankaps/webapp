from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required
from app.blueprints import customer


# Customer dashboard route
@customer.route('/customer/settings')
@login_required
def settings():
    if current_user.role == "administrator":
        return redirect(url_for('admin.dashboard'))
    return render_template('customer/settings.html')
