from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app(config=None):
	app = Flask(__name__)

	if app.config["ENV"] == 'production':
		app.config.from_object('config.ProductionConfig')
	else:
		app.config.from_object('config.DevelopmentConfig')
		
	if config is not None:
		app.config.update(config)
	
	db.init_app(app)
	migrate.init_app(app, db)

	from cart_app.routes import (main_route, cart_route, compare_route)
	app.register_blueprint(main_route.bp)
	app.register_blueprint(cart_route.bp)
	app.register_blueprint(compare_route.bp)

	return app

if __name__ == "__main__":
	# 배포 위한 포트 설정
	port = int(os.environ.get("PORT", 33507))
	app = create_app()
	app.run(host="0.0.0.0", port=port)
