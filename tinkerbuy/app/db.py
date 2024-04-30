import os
from flask_sqlalchemy import SQLAlchemy

# Create SQLAlchemy database instance
db = SQLAlchemy()

# Configure database connection URI
def configure_db(app):
    # Get database URI from environment variable or config file
    db_uri = os.environ.get('DATABASE_URL') or app.config['SQLALCHEMY_DATABASE_URI']

    # Set database URI
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

    # Initialize database
    db.init_app(app)

    # Create all database tables if they don't exist
    with app.app_context():
        db.create_all()