from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from app.blueprints import auth

# index page
@auth.route('/')
def index():
    return render_template('index.html')


# auth registration route
@auth.route('/register/', methods=['GET', 'POST'])
@auth.route('/signup/', methods=['GET', 'POST'])
def register():
    '''
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Hash password
        hashed_password = generate_password_hash(password)

        # Create new customer
        new_customer = Customer(name=name, email=email, password=hashed_password)

        # Add customer to database
        db.session.add(new_customer)
        db.session.commit()

        # Flash success message
        flash('Customer registered successfully!', 'success')

        # Redirect to login page
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html')
    '''
    return render_template("auth/signup.html")

# auth login route
@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    if request.method == 'POST':
        # Get form data
        email = request.form['email']
        password = request.form['password']

        # Get customer from database
        customer = Customer.query.filter_by(email=email).first()

        # Check if customer exists and password is correct
        if customer and check_password_hash(customer.password, password):
            login_user(customer)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('customer.dashboard'))
        else:
            flash('Invalid email or password.', 'danger')

    return render_template('customer/login.html')
"""
    return "AUTH LOGIN"

# Customer logout route
@auth.route('/logout/')
#@login_required
def logout():
    '''
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('auth.login'))
    '''
    return "AUTH LOGOUT"

