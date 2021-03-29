from cart_app import db

class Cart(db.Model):
	__tablename__ = 'cart'

	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String())
	itemcode = db.Column(db.String())
	myprice = db.Column(db.Integer())
	product_id = db.Column(db.Integer(), db.ForeignKey('product.id'))

	def __repr__(self):
		return f"Cart {self.id}"
