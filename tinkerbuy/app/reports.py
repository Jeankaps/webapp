from flask import render_template, request, flash, redirect, url_for, send_file
from flask_login import login_required
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from app.blueprints import orders
from app.blueprints import reports
from app.models import *

@reports.route('/reports/sales', methods=['POST'])
@login_required
#def generate_sales_report(start_date, end_date):
def generate_sales_report():
   
    # Filter order items based on the date range
    #order_items = OrderItem.query.join(Order).filter(Order.created_at >= start_date, Order.created_at <= end_date).all()
    order_items = OrderItem.query.join(Order).all()

    # Calculate total revenue and total orders
    total_revenue = sum(item.quantity * item.product.price for item in order_items)
    total_orders = len(set(item.order_id for item in order_items))

    # Calculate product-wise sales
    product_sales = {}
    for item in order_items:
        product_sales.setdefault(item.product.name, 0)
        product_sales[item.product.name] += item.quantity * item.product.price
    '''
    # Create a dictionary with the calculated data
    sales_report = {
        #'start_date': start_date,
        #'end_date': end_date,
        'total_revenue': total_revenue,
        'total_orders': total_orders,
        'product_sales': product_sales
    }
   # Convert the dictionary to a pandas DataFrame
    df = pd.DataFrame.from_dict(sales_report, orient='index', columns=['Value'])

    # Write the DataFrame to a CSV file
    csv_path = 'app/reports/sales_reports.csv'
    df.to_csv(csv_path)
    send_file_path = 'reports/sales_reports.csv'
'''
    # Combine DataFrames
    sales_report = {
        'total_revenue': total_revenue,
        'total_orders': total_orders,
    }

    # Convert the dictionary to a pandas DataFrame
    df = pd.DataFrame.from_dict(sales_report, orient='index', columns=['Value'])

    # Write the DataFrame to a CSV file
    csv_path = "/tmp/sales_reports.csv"
    df.to_csv(csv_path, index=False)  # Don't include index row in CSV
    send_file_path = '/tmp/sales_reports.csv'

    # send the file to the user

    return send_file(send_file_path, as_attachment=True)

'''
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
'''
'''
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
    '''