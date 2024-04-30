from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required
from app.blueprints import products
from app.models import Product


# Product list route
@products.route('/products')
def product_list():
    products = Product.query.all()
    return render_template('product/list.html', products=products)
'''
# Product create route
@products.route('/products/create', methods=['GET', 'POST'])
@login_required
def product_create():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        quantity = request.form['quantity']

        # Create new product
        new_product = Product(name=name, description=description, price=price, quantity=quantity)

        # Add product to database
        db.session.add(new_product)
        db.session.commit()

        # Flash success message
        flash('Product created successfully!', 'success')

        # Redirect to product list page
        return redirect(url_for('products.product_list'))

    return render_template('product/create.html')

# Product edit route
@products.route('/products/<int:product_id>/edit', methods=['GET', 'POST'])
@login_required
def product_edit(product_id):
    product = Product.query.get_or_404(product_id)

    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        quantity = request.form['quantity']

        # Update product
        product.name = name
        product.description = description
        product.price = price
        product.quantity = quantity

        # Save changes to database
        db.session.commit()

        # Flash success message
        flash('Product updated successfully!', 'success')

        # Redirect to product list page
        return redirect(url_for('products.product_list'))

    return render_template('product/edit.html', product=product)

# Product delete route
@products.route('/products/<int:product_id>/delete', methods=['POST'])
@login_required
def product_delete(product_id):
    product = Product.query.get_or_404(product_id)

    # Delete product
    db.session.delete(product)
    db.session.commit()

    # Flash success message
    flash('Product deleted successfully!', 'success')

    # Redirect to product list page
    return redirect(url_for('products.product_list'))
    '''