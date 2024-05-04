from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from app.blueprints import orders
from app import db 
from app.models import Order


# Order create route
@orders.route('/orders/create', methods=['GET', 'POST'])
@login_required
def order_create():
    if request.method == 'POST':
        # Get form data
        customer_id = current_user.id
        product_id = request.form['product_id']
        quantity = request.form['quantity']

        # Create new order
        new_order = Order(customer_id=customer_id, product_id=product_id, quantity=quantity)

        # Add order to database
        db.session.add(new_order)
        db.session.commit()

        # Flash success message
        flash('Order created successfully!', 'success')

        # Redirect to order list page
        return redirect(url_for('orders.order_list'))

    return render_template('customer/create.html')

# Order list route
@orders.route('/orders')
@login_required
def order_list():
    orders = Order.query.filter_by(customer_id=current_user.id).all()
    return render_template('orders.html', orders=orders)
'''
# Order edit route
@orders.route('/orders/<int:order_id>/edit', methods=['GET', 'POST'])
@login_required
def order_edit(order_id):
    order = Order.query.get_or_404(order_id)

    if request.method == 'POST':
        # Get form data
        quantity = request.form['quantity']

        # Update order
        order.quantity = quantity

        # Save changes to database
        db.session.commit()

        # Flash success message
        flash('Order updated successfully!', 'success')

        # Redirect to order list page
        return redirect(url_for('orders.order_list'))

    return render_template('order/edit.html', order=order)
'''
# Order delete route
@orders.route('/orders/<int:order_id>/delete', methods=['POST'])
@login_required
def order_delete(order_id):
    order = Order.query.get_or_404(order_id)

    # Delete order
    db.session.delete(order)
    db.session.commit()

    # Flash success message
    flash('Order deleted successfully!', 'success')

    # Redirect to order list page
    return redirect(url_for('orders.order_list'))