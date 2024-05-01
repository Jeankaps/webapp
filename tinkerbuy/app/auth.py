from flask import  render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from app.blueprints import auth
from app.forms import RegisterForm, LoginForm
from app.models import User
from app import db 

# index page
@auth.route('/')
def index():
    return render_template('index.html')


# auth registration route
@auth.route('/register/', methods=['GET', 'POST'])
@auth.route('/signup/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if  form.validate_on_submit():
        hashed_password = generate_password_hash(form.password1.data)
        new_user = User(name = form.username.data,
                    email = form.email_address.data,
                    password = hashed_password)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        flash(f'Account registered successfully!', 'success')
        return redirect(url_for( 'products.product_list' ))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(err_msg, 'danger')
    return render_template("auth/signup.html", form=form)

# auth login route
@auth.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.username.data).first()
        if user and user.check_password(password=form.password.data):
            login_user(user)
            flash(f'Succes! You are logged in as: {user.name}', category='success')
            if current_user.role == 'administrator':
                return redirect(url_for('admin.dashboard'))
            return redirect(url_for('products.product_list'))
        else:
            flash('Username or password is not correct. Please, try again.', category='danger')

    return render_template('auth/login.html', form=form)

# Customer logout route
@auth.route('/logout/')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('auth.index'))

