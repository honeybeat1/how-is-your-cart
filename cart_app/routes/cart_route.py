from flask import Blueprint, render_template, request, redirect, url_for
from cart_app.models.cart_model import Cart
from cart_app.models.product_model import Product
from cart_app.utils import main_funcs
from cart_app import db

bp = Blueprint('cart', __name__)

@bp.route('/cart')
def cart_index():
	""" 카트에 담긴 농수산물 조회 """

	msg_code = request.args.get('msg_code', None)
	alert_msg = main_funcs.msg_processor(msg_code) if msg_code is not None else None
	
	#cart_table에 있는 상품 모두 조회하기 # type() = List
	carts = Cart.query.all()

	# 템플릿 파일에 넘겨줄 수 있게 맞춰서 넘겨주기
	cart_list = []
	for p_cart in carts:
		cart = {}
		cart['id'] = p_cart.id
		cart['name'] = p_cart.name
		cart['itemcode'] = p_cart.itemcode
		cart['myprice'] = p_cart.myprice
		cart_list.append(cart)
	
	return render_template('cart.html', alert_msg=alert_msg, cart_list=cart_list)

@bp.route('/cart', methods=['POST'])
def add_cart():
	""" 카트에 가격을 알고 싶은 농수산물을 담습니다 """
	try:
		name = request.form['name']
		price = request.form['price']
	except:
		return "Needs product name", 400
	
	if len(name)==0: #상품을 입력하지 않은 경우
		return redirect(url_for('cart.cart_index', msg_code=5))
	if len(price)==0: #가격을 입력하지 않은 경우
		# if price is None으로 했을 때 안잡힌다
		return redirect(url_for('cart.cart_index', msg_code=6))
	try:
		int(price)
	except: # 숫자외에 입력되었을 경우
		return redirect(url_for('cart.cart_index', msg_code=6))
	
	# db에서 price 조회하기
	p_product = Product.query.filter(Product.name==name).first()
	if p_product:
		n_cart = Cart(name=name, itemcode=p_product.itemcode, myprice=price)
		db.session.add(n_cart)
		db.session.commit()
	else: # db에 해당 이름을 가진 상품이 없을 경우
		return redirect(url_for('cart.cart_index', msg_code=4))
		
	return redirect(url_for('cart.cart_index', msg_code=0))

@bp.route('/cart/')
@bp.route('/cart/<int:cart_id>')
def delete_cart(cart_id=None):
	"""해당 id 값을 갖고 있는 카트에 담긴 상품을 삭제합니다"""
	if cart_id is None:
		return Response(status=400)
	else:
		p_cart = Cart.query.filter(Cart.id==cart_id).first()
		if not p_cart:
			return Response(status=404)
		else:
			db.session.delete(p_cart)
			db.session.commit()
	return redirect(url_for('cart.cart_index', msg_code=3))
