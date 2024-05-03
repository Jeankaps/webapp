from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField, SelectField, IntegerField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError,NumberRange
from .models import User


class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(name=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address')

    username = StringField(label='Username:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    username = StringField(label='Username:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase Item!')

class SearchFilterForm(FlaskForm):
    query = StringField(label="Search" )
    submit = SubmitField(label="q")


class CreditCardForm(FlaskForm):
    card_number = StringField(label='Card Number', validators=[DataRequired(), Length(min=16, max=16)])
    card_holder = StringField('Card Holder', validators=[DataRequired(), Length(max=100)])
    expiration_month = SelectField('Expiration Month', choices=[(str(i), str(i)) for i in range(1, 13)], validators=[DataRequired()])
    expiration_year = SelectField('Expiration Year', choices=[(str(i), str(i)) for i in range(2024, 2034)], validators=[DataRequired()])
    cvv = IntegerField('CVV', validators=[DataRequired(), NumberRange(min=100, max=999)])
    submit = SubmitField(label="PAY NOW")

    