from flask import Blueprint, render_template
from flask_login import login_required
from app.blueprints import admin 


# Admin dashboard route
@admin.route('/admin/')
#@login_required
def dashboard():
    return render_template('admin/dashboard.html')