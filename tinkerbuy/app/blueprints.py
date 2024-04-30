from flask import Blueprint

admin = Blueprint('admin', __name__,template_folder='templates')
customer = Blueprint('customer', __name__)
auth = Blueprint('auth', __name__)
cart = Blueprint('cart', __name__)
products = Blueprint('products', __name__)