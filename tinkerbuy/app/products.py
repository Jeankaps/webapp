from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required
from flask_pagination import Pagination
from app.blueprints import products
from app.models import Product


# Product list route
@products.route('/products', methods=['GET','POST'])
@login_required
def product_list():
    # Get the page number from query parameters, default to 1
    page = request.args.get('page', 1, type=int)

    # Define the number of products per page
    per_page = 10

    # Get the search query from request parameters
    query = request.args.get('q')

    # Filter products based on the search query
    if query:
        products = Product.query.filter(Product.name.ilike(f"%{query}%"))
    else:
        products = Product.query

    # Paginate the products
    paginated_products = products.paginate(page=page, per_page=per_page)

    return render_template('product/list.html', products=paginated_products.items, paginated_products=paginated_products)
    

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