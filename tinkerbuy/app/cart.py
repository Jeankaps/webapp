from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from app.blueprints import cart
from app.models import Product, Order,OrderItem,Payment
from app import db 


# Cart view route
@cart.route('/cart/')
@login_required
def cart_view():
    # Get cart items for current user
    cart_items = current_user.cart_items
    print(f'Type => {type(cart_items)}')

    # Calculate total price
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    return render_template('cart.html', cart_items=cart_items, total_price=total_price)

# Cart add item route
@cart.route('/cart/add/<int:product_id>', methods=['GET','POST'])
@login_required
def cart_add(product_id):
    # Get product from database
    product = Product.query.get_or_404(product_id)

    # Add product to cart
    current_user.add_to_cart(product)

    # Flash success message
    flash('Product added to cart!', 'success')

    return redirect(url_for('products.product_list'))

# Cart remove item route
@cart.route('/cart/remove/<int:product_id>', methods=['POST'])
@login_required
def cart_remove(product_id):
    # Get product from database
    product = Product.query.get_or_404(product_id)

    # Remove product from cart
    current_user.remove_from_cart(product)

    # Flash success message
    flash('Product removed from cart!', 'success')

    return redirect(url_for('cart.cart_view'))

'''
# Cart update quantity route
@cart.route('/cart/update/<int:product_id>', methods=['POST'])
@login_required
def cart_update(product_id):
    # Get product from database
    product = Product.query.get_or_404(product_id)

    # Get new quantity from form
    quantity = request.form['quantity']

    # Update cart item quantity
    current_user.update_cart_item(product, quantity)

    # Flash success message
    flash('Cart item quantity updated!', 'success')

    return redirect(url_for('cart.cart_view'))

    '''
# Cart checkout route
@cart.route('/cart/checkout')
@login_required
def cart_checkout():
    # Get cart items for current user
    cart_items = current_user.cart_items

    # Calculate total price
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    # Create new order
    new_order = Order(customer_id=current_user.id)

    # Add cart items to order
    for item in cart_items:
        new_order.order_items.append(OrderItem(product_id=item.product.id, quantity=item.quantity))

    # Create new payment
    new_payment = Payment(order_id=new_order.id, amount=total_price, payment_method='Cash')

    # Add order and payment to database
    db.session.add(new_order)
    db.session.add(new_payment)
    db.session.commit()

    # Clear cart
    current_user.clear_cart()

    # Flash success message
    flash('Order placed successfully!', 'success')

    return redirect(url_for('orders.order_list'))