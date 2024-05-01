from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from app.blueprints import admin 


# Admin dashboard route
@admin.route('/admin/')
@login_required
def dashboard():
    if current_user.name == "admin": # the use is an admin
        return render_template('admin/dashboard.html')
    else:
        return redirect(url_for( 'auth.index '))