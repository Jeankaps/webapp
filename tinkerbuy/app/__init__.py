from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS
from config import app_config 

# Create Flask app instance
app = Flask(__name__)

# Load configuration from config.py
app.config.from_object('config.app_config')

# Initialize database
db = SQLAlchemy(app)

# Import models
from app.models import User, Product, Order, Payment, CartItem, OrderItem 

# Create database tables if they don't exist
with app.app_context():
    db.create_all()

'''
# Initialize login manager
login_manager = LoginManager(app)
login_manager.login_view = 'customer.login'

# Initialize migration engine
migrate = Migrate(app, db)

# Initialize RESTful API
api = Api(app)

# Initialize CORS
CORS(app)
'''
# Import blueprints
from app.blueprints import auth
from app.blueprints import admin
from app.blueprints import customer
from app.blueprints import cart
'''
from app.products import products
from app.orders import orders
from app.payments import payments
from app.reports import reports
'''
# Import views 
from app.admin import * 
from app.auth import *
from app.cart import *
from app.customer import * 

# Register blueprints
app.register_blueprint(admin, url_prefix="/")
app.register_blueprint(customer)
app.register_blueprint(auth)
app.register_blueprint(cart) # need a prefix like /logged_in_User 
'''
app.register_blueprint(products)
app.register_blueprint(orders)
app.register_blueprint(payments)
app.register_blueprint(reports)
'''