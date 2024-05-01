from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required

# Create blueprint
inventory = Blueprint('inventory', __name__)
'''
# Inventory view route
@inventory.route('/inventory')
@login_required
def inventory_view():
    # Get all products
    products = Product.query.all()

    return render_template('inventory/inventory.html', products=products)

# Inventory update quantity route
@inventory.route('/inventory/update/<int:product_id>', methods=['POST'])
@login_required
def inventory_update(product_id):
    # Get product from database
    product = Product.query.get_or_404(product_id)

    # Get new quantity from form
    quantity = request.form['quantity']

    # Update product quantity
    product.quantity = quantity

    # Save changes to database
    db.session.commit()

    # Flash success message
    flash('Product quantity updated!', 'success')

    return redirect(url_for('inventory.inventory_view'))
    '''