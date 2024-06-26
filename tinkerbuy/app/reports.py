from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create blueprint
reports = Blueprint('reports', __name__)

# Sales report route
@reports.route('/reports/sales')
@login_required
def sales_report():
    # Get all orders
    orders = Order.query.all()

    # Convert orders to pandas DataFrame
    df_orders = pd.DataFrame([order.to_dict() for order in orders])

    # Calculate total sales and average order value
    total_sales = df_orders['amount'].sum()
    avg_order_value = df_orders['amount'].mean()

    # Group orders by product and calculate total sales per product
    df_product_sales = df_orders.groupby('product_id').agg({'amount': 'sum'})

    # Get top 5 selling products
    top_5_products = df_product_sales.sort_values(by='amount', ascending=False).head(5)

    # Generate sales report
    report = {
        'total_sales': total_sales,
        'avg_order_value': avg_order_value,
        'top_5_products': top_5_products.to_dict(),
    }

    return render_template('reports/sales.html', report=report)

# Inventory report route
@reports.route('/reports/inventory')
@login_required
def inventory_report():
    # Get all products
    products = Product.query.all()

    # Convert products to pandas DataFrame
    df_products = pd.DataFrame([product.to_dict() for product in products])

    # Calculate total inventory value
    total_inventory_value = df_products['price'] * df_products['quantity']

    # Generate inventory report
    report = {
        'total_inventory_value': total_inventory_value,
        'products': df_products.to_dict(orient='records'),
    }

    return render_template('reports/inventory.html', report=report)

# Customer report route
@reports.route('/reports/customers')
@login_required
def customer_report():
    # Get all customers
    customers = User.query.all()

    # Convert customers to pandas DataFrame
    df_customers = pd.DataFrame([customer.to_dict() for customer in customers])

    # Calculate number of orders per customer
    df_customer_orders = df_customers.merge(pd.DataFrame([order.to_dict() for order in Order.query.all()]), on='id', how='left')
    df_customer_orders = df_customer_orders.groupby('customer_id').agg({'id': 'count'})

    # Generate customer report
    report = {
        'customers': df_customers.to_dict(orient='records'),
        'customer_orders': df_customer_orders.to_dict(),
    }

    return render_template('reports/customers.html', report=report)