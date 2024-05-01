from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from app.blueprints import admin
from app.models import User, Card, Payment, CartItem, Order, OrderItem
from app import db 


# Admin dashboard route
@admin.route('/admin/')
@login_required
def dashboard():
    if current_user.role == "administrator": # the use is an admin
        # Get all Users
        users = User.query.all()

        return render_template('admin/dashboard.html', users=users)
    else:
        return redirect(url_for( 'auth.index'))

# Remove user
@admin.route('/admin/<int:user_id>/delete', methods=['POST'])
@login_required
def delete_user(user_id):
    if current_user.role == 'administrator':
        # Get user to delete 
        user = User.query.get_or_404(user_id)
        # delete all cart items associated with the user
        CartItem.query.filter_by(user_id=user_id).delete()
        # Delete all orders
        Order.query.filter_by(customer_id=user_id).delete()
        # delete all payments
        Card.query.filter_by(customer_id=user_id).delete()
        # delete user
        db.session.delete(user)
        db.session.commit()

        # Pass variable to display remaining users
        users = User.query.all()
        return render_template('admin/dashboard.html', users=users)
    else:
        return redirect(url_for( 'auth.index'))