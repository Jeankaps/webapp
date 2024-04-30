from flask import Blueprint, render_template
from flask_login import login_required

# Create blueprint
admin = Blueprint('admin', __name__)

# Admin dashboard route
@admin.route('/admin')
@login_required
def dashboard():
    return render_template('admin/dashboard.html')