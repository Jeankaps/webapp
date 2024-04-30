import os
class Config():
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql://root:hardtoguess@172.17.0.1/development'

    # Secret key for session management
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev'

    # Flask-WTF configuration
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = os.environ.get('WTF_CSRF_SECRET_KEY') or 'dev'

    # Flask-Login configuration
    LOGIN_DISABLED = False

    # Flask-RESTful configuration
    RESTFUL_JSON = {'indent': 4}

    # CORS configuration
    CORS_HEADERS = 'Content-Type'
    
app_config = Config()