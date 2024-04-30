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
'''
# Configure database
from db import configure_db
configure_db(app)

# Initialize database
db = SQLAlchemy(app)

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
'''
# Import blueprints
from app.admin import admin
from app.customer import customer
from app.products import products
from app.orders import orders
from app.payments import payments
from app.reports import reports

# Register blueprints
app.register_blueprint(admin)
app.register_blueprint(customer)
app.register_blueprint(products)
app.register_blueprint(orders)
app.register_blueprint(payments)
app.register_blueprint(reports)
'''
'''
# Import models
from app.models import User, Product, Order, Payment, Report

# Create database tables if they don't exist
with app.app_context():
    db.create_all()
'''