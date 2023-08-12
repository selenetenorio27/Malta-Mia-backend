from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.cliente import Cliente
from app.models.favoritos import Favoritos
from app.models.cerveza import Cerveza
from app.routes.cerveza_routes import validate_model

favoritos_bp = Blueprint("favoritos_bp", __name__, url_prefix="/favoritos")

@favoritos_bp.route("/<cliente_id>", methods=["GET"])
def get_cliente_favoritos(cliente_id):
    cliente = validate_model(Cliente, cliente_id)
    
    favoritos_response = []
    for favorito in cliente.favoritos:
        favoritos_response.append(favorito.cerveza.to_dict())
    
    return jsonify(favoritos_response), 200


@favoritos_bp.route("", methods=["POST"])
def add_favorite():
    data = request.json  
    cliente_id = data.get('cliente_id')
    cerveza_id = data.get('cerveza_id')

    favorito = Favoritos(cliente_id=cliente_id, cerveza_id=cerveza_id)

    try:
        db.session.add(favorito)
        db.session.commit()
        return jsonify({'message': 'Cerveza agregada a favoritos'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Error al agregar la cerveza a favoritos: ' + e}), 500
