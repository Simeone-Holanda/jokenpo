from flask import Flask
from os import path
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'my secret_key '
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # db = SQLAlchemy()
    # migrate = Migrate(app, db)

    from .routes import views

    app.register_blueprint(views, url_prefix='/')

    return app
