from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required
from app.blueprints import payments
from app import db

# Payment create route
@payments.route('/payments/create', methods=['GET', 'POST'])
@login_required
def payment_create():
    if request.method == 'POST':
        # Get form data
        order_id = request.form['order_id']
        amount = request.form['amount']
        payment_method = request.form['payment_method']

        # Create new payment
        new_payment = Payment(order_id=order_id, amount=amount, payment_method=payment_method)

        # Add payment to database
        db.session.add(new_payment)