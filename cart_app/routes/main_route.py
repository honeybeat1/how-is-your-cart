from flask import Blueprint, render_template, request
import pandas as pd
from datetime import datetime
import jinja2
from cart_app.services.price_api import get_products
from cart_app.models.product_model import Product
from cart_app import db

bp = Blueprint('main', __name__)

# @bp.route('/')
# def index():
# 	""" Home page """
# 	return render_template('index.html')

@bp.route('/')
def loading():
	return render_template('loading.html');

@bp.route('/main')
def add_price_data():
	""" 오늘 기준 가격 데이터를 api에서 호출한 뒤 
		DB에 저장합니다 """
	df = pd.DataFrame()
	date = datetime.today()
	api_template = jinja2.Template("{{ date.strftime('%Y-%m-%d') }}")
	
	df = get_products(date=date)
	# 한 row씩 DB에 저장합니다.
	for row in df.values:
		n_product = Product(name=row[0], itemcode=row[1], kindname=row[2], unit=row[4], price=row[5],
							day_bf_price=row[6], week_bf_price=row[7], two_week_bf_price=row[8], month_bf_price=row[9])
		db.session.add(n_product)
		db.session.commit()
	return render_template('index.html')
