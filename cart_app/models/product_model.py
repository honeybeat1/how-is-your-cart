from cart_app import db

class Product(db.Model):
	__tablename__ : 'product'

	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String())
	itemcode = db.Column(db.String())
	kindname = db.Column(db.String())
	unit = db.Column(db.String())
	price = db.Column(db.Integer())
	day_bf_price = db.Column(db.Integer())
	week_bf_price = db.Column(db.Integer())
	two_week_bf_price = db.Column(db.Integer())
	month_bf_price = db.Column(db.Integer())
	carts = db.relationship('Cart', backref='product', cascade='delete')

	def __repr__(self):
		return f"Product {self.id}"
