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

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "SQLALCHEMY_DATABASE_URI")
    
    from app.models.cerveza import Cerveza
    from app.models.cliente import Cliente
    from app.models.encuesta import Encuesta
    from app.models.favoritos import Favoritos
    
    db.init_app(app)

    #Agregado para crear base de datos con las cervezas
    # with app.app_context():
    #     db.create_all()
    #     agregar_cervezas_iniciales()

    #Instancias de cervezas
    # cerveza1 = Cerveza(nombre='Dark Lager', marca='Principia',porcentaje_alcohol=4.0, estilo='lager', ibus=22, color='obscura', sabor='Caramelo y tostado', ingrediente_adicional='cafe')
    # cerveza2 = Cerveza(nombre='American Wheat Ale', marca='Principia',porcentaje_alcohol=4.3, estilo='wheat ale', ibus=18, color='clara', sabor='Ligero y refrescante', ingrediente_adicional='ninguno')

    # db.session.add(cerveza1)
    # db.session.add(cerveza2)
    # db.session.commit()

    #Aqui termina el codigo para crear la base de datos


    migrate.init_app(app, db)

    from .routes.cerveza_routes import cervezas_bp
    app.register_blueprint(cervezas_bp)

    CORS(app)
    return app