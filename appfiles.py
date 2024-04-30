import os

def create_file_structure():
    """Creates the file structure for the TinkerBuy web application."""

    # Create the main directories
    directories = [
        "tinkerbuy",
        "tinkerbuy/app",
        "tinkerbuy/migrations/versions",
        "tinkerbuy/static/css",
        "tinkerbuy/static/js",
        "tinkerbuy/static/img",
        "tinkerbuy/templates",
        "tinkerbuy/templates/admin",
        "tinkerbuy/tests",
    ]

    for directory in directories:
        os.makedirs(directory, exist_ok=True)

    # Create the files
    files = [
        "tinkerbuy/__init__.py",
        "tinkerbuy/app/__init__.py",
        "tinkerbuy/app/admin.py",
        "tinkerbuy/app/cart.py",
        "tinkerbuy/app/customer.py",
        "tinkerbuy/app/inventory.py",
        "tinkerbuy/app/models.py",
        "tinkerbuy/app/orders.py",
        "tinkerbuy/app/payments.py",
        "tinkerbuy/app/products.py",
        "tinkerbuy/app/reports.py",
        "tinkerbuy/app/utils.py",
        "tinkerbuy/config.py",
        "tinkerbuy/db.py",
        "tinkerbuy/migrations/__init__.py",
        "tinkerbuy/requirements.txt",
        "tinkerbuy/run.py",
        "tinkerbuy/static/css/style.css",
        "tinkerbuy/static/js/script.js",
        "tinkerbuy/templates/base.html",
        "tinkerbuy/templates/cart.html",
        "tinkerbuy/templates/customer/base.html",
        "tinkerbuy/templates/customer/create.html",
        "tinkerbuy/templates/customer/delete.html",
        "tinkerbuy/templates/customer/edit.html",
        "tinkerbuy/templates/customer/login.html",
        "tinkerbuy/templates/index.html",
        "tinkerbuy/templates/orders.html",
        "tinkerbuy/templates/product/base.html",
        "tinkerbuy/templates/product/create.html",
        "tinkerbuy/templates/product/delete.html",
        "tinkerbuy/templates/product/edit.html",
        "tinkerbuy/templates/product/list.html",
        "tinkerbuy/templates/payments.html",
        "tinkerbuy/tests/__init__.py",
        "tinkerbuy/tests/test_admin.py",
        "tinkerbuy/tests/test_cart.py",
        "tinkerbuy/tests/test_customer.py",
        "tinkerbuy/tests/test_inventory.py",
        "tinkerbuy/tests/test_models.py",
        "tinkerbuy/tests/test_orders.py",
        "tinkerbuy/tests/test_payments.py",
        "tinkerbuy/tests/test_products.py",
        "tinkerbuy/tests/test_reports.py",
    ]

    for file in files:
        with open(file, "w"):
            pass

if __name__ == "__main__":
    create_file_structure()