from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from app.blueprints import cart
from app.forms import CreditCardForm,LoginForm
from app.models import Product, Order,OrderItem,Payment, CartItem, Card
from app import db 


# Cart view route
@cart.route('/cart/')
@login_required
def cart_view():
    # Get cart items for current user
    cart_items = current_user.cart_items
    basket = dict()
    for item in cart_items:
        product = Product.query.filter_by(id=item.product_id).first() 
        qty = item.quantity
        basket[product] = qty
    
    # Calculate total price
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    return render_template('cart.html', basket=basket, total_price=total_price)

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
@cart.route('/cart/remove/<int:product_id>/', methods=['GET','POST'])
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
@cart.route('/cart/checkout', methods=['GET','POST'])
@login_required
def cart_checkout():
    form = CreditCardForm()
    if form.validate_on_submit():
        # Create a new card for the customer
        exp_date_str = f"{form.expiration_year.data}-{form.expiration_month.data}-01"

        # We don't need a new card if one already exists. Will do this later.
        card = Card(
            customer_id=current_user.id,
            card_number = form.card_number.data,
            exp_date = exp_date_str,
            CVV = form.cvv.data,
            cardholder_name = form.card_holder.data
            )
        # Get cart items for current user
        cart_items = current_user.cart_items

        # Calculate total price
        total_price = sum(item.product.price * item.quantity for item in cart_items)

        # Create new order
        new_order = Order(customer_id=current_user.id)

        # Add cart items to order
        for item in cart_items:
            new_order.order_items.append(OrderItem(product_id=item.product_id, quantity=item.quantity))

        # Add card and order to the database
        db.session.add(card)
        db.session.add(new_order)
        db.session.commit()

        # This will need to be rewritten, but for now, we need order_id 
        # and card_id to create Payment object 
        # We get it from db
        card_id = Card.query.filter_by(customer_id=card.customer_id, card_number=card.card_number).first().id
        order_id = Order.query.filter_by(customer_id=new_order.customer_id, created_at=new_order.created_at).first().id

        # Create new payment
        new_payment = Payment(order_id=order_id, card_id=card_id, amount=total_price, payment_method='Cash')

        # Add order and payment to database
        db.session.add(new_payment)
        db.session.commit()

        # Clear cart
        current_user.clear_cart()

        # Flash success message
        flash('Order placed successfully!', 'success')

        return redirect(url_for('orders.order_list'))
    return render_template('checkout.html', form=form)