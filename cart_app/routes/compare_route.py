from flask import Blueprint, render_template, request
from cart_app.utils import main_funcs
from cart_app.models.cart_model import Cart
from cart_app.models.product_model import Product

bp = Blueprint('compare', __name__)

@bp.route('/compare', methods=["GET", "POST"])
def compare_index():
	""" 카트에 담긴 식재료들의 가격과 공시 가격간의 비교 """
	# 카트에 담긴 식재료 가져오기
	cart_lst = Cart.query.all()

	carts = [{'id':cart.id, 'name':cart.name, 'price':cart.myprice} for cart in cart_lst]
	comparison= None
	p_product= None

	# 카트에 담긴 식재료 하나 가져왔다면
	if request.method == "POST":
		cart_name = request.form['name']
		p_cart = Cart.query.filter(Cart.name==cart_name).first()
		p_product = Product.query.filter(Product.name==cart_name).first()
		comparison = p_cart.myprice - p_product.price

	return render_template('compare.html', carts=carts, comparison=comparison, product=p_product)
