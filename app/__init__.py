from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_marshmallow import Marshmallow

app = Flask(__name__)  # app
db = SQLAlchemy()  # bd
ma = Marshmallow(app)  # serializador


def create_app():

    app.config['SECRET_KEY'] = 'askdjanbsdlknjasd'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .models.jogador import Jogador
    from .models.jogada import Jogada

    from flask_migrate import Migrate
    
    migrate = Migrate(app, db)  # Config das migrações

    from .routes.routes_round import views_round
    from .routes.routes_player import views_player

    app.register_blueprint(views_round, url_prefix='/')
    app.register_blueprint(views_player, url_prefix='/')

    return app
