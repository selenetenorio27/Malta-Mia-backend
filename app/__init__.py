from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS


db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    #     "SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("RENDER_DATABASE_URI")
    
    from app.models.cerveza import Cerveza
    from app.models.cliente import Cliente
    from app.models.encuesta import Encuesta
    from app.models.favoritos import Favoritos
    
    db.init_app(app)


    migrate.init_app(app, db)

    from .routes.cerveza_routes import cervezas_bp
    app.register_blueprint(cervezas_bp)
    from .routes.favorito_routes import favoritos_bp
    app.register_blueprint(favoritos_bp)

    CORS(app)
    return app