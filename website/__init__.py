from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"




def create_app():
	app=Flask(__name__)
	app.config['SECRET_KEY'] = '2441139hrit'
	app.config['SQL_ALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
	db.init_app(app)

	from .views import views
	from .auth import auth

	app.register_blueprint(views,url_prefix="/")
	app.register_blueprint(auth,url_prefix="/")

	form .models import User

	create_database(app)

	return app

def create_database():
	if not path.exists('website/'+ DB_NAME):
		db.create_all(app=app)

		print("database created")