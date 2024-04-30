from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timezone 
from app import db

# User model
class User(UserMixin, db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), default='customer')
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, onupdate=lambda: datetime.now(timezone.utc))

    # Set password
    def set_password(self, password):
        self.password = generate_password_hash(password)

    # Check password
    def check_password(self, password):
        return check_password_hash(self.password, password)

    # Add to cart helper method
    def add_to_cart(self, product):
        cart_item = CartItem.query.filter_by(user_id=self.id, product_id=Product.id).first()
        if cart_item:
            cart_item.quantity += 1
        else:
            cart_item = CartItem(user_id=self.id, product_id=Product.id, quantity=1)
        db.session.add(cart_item)
        db.session.commit()

    # Remove from cart helper method
    def remove_from_cart(self, product):
        cart_item = CartItem.query.filter_by(user_id=self.id, product_id=Product.id).first()
        if cart_item:
            db.session.delete(cart_item)
            db.session.commit()

    # Update cart item quantity helper method
    def update_cart_item(self, product, quantity):
        cart_item = CartItem.query.filter_by(user_id=self.id, product_id=Product.id).first()
        if cart_item:
            cart_item.quantity = quantity
            db.session.commit()

    # Clear cart helper method
    def clear_cart(self):
        cart_items = CartItem.query.filter_by(user_id=self.id).all()
        for cart_item in cart_items:
            db.session.delete(cart_item)
        db.session.commit()

    # Relationship with CartItem model
    cart_items = db.relationship('CartItem', backref='customer', lazy='dynamic')

    # Relationship with Order model
    orders = db.relationship('Order', backref='customer', lazy='dynamic')

# Product model
class Product(db.Model):
    __tablename__ = 'Product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(datetime.timezone.utc))
    updated_at = db.Column(db.DateTime, onupdate=lambda: datetime.now(datetime.timezone.utc))

    # Relationship with OrderItem model
    order_items = db.relationship('OrderItem', backref='product', lazy='dynamic')

# Order model
class Order(db.Model):
    __tablename__ = 'Order'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(datetime.timezone.utc))

    # Relationship with OrderItem model
    order_items = db.relationship('OrderItem', backref='order', lazy='dynamic')

# OrderItem model
class OrderItem(db.Model):
    __tablename__ = 'OrderItem'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('Order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('Product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Payment model
class Payment(db.Model):
    __tablename__ = 'Payment'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('Order.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.String(255), nullable=False)
    card_id = db.Column(db.Integer, db.ForeignKey('Card.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(datetime.timezone.utc))

# Card model
class Card(db.Model):
    __tablename__ = 'Card'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    card_number = db.Column(db.String(19), nullable=False)
    exp_date = db.Column(db.DateTime, nullable=False)
    CVV = db.Column(db.String(3), nullable=False)
    cardholder_name = db.Column(db.String(255), nullable=False)
    billing_address = db.Column(db.String(255), nullable=False)
    credit_limit = db.Column(db.Numeric(10,2), nullable=False)

# CartItem model
class CartItem(db.Model):
    __tablename__ = 'CartItem'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('Product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)