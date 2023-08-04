from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.cliente import Cliente
from app.models.favoritos import Favoritos
from app.models.cerveza import Cerveza
from app.routes.cerveza_routes import validate_model

clientes_bp = Blueprint("clientes_bp", __name__, url_prefix="/clientes")

@clientes_bp.route("/<cliente_id>/favoritos", methods=["GET"])
def get_cliente_favoritos(cliente_id):
    cliente = validate_model(Cliente, cliente_id)
    
    favoritos_response = []
    for favorito in cliente.favoritos:
        favoritos_response.append(favorito.cerveza.to_dict())
    
    return jsonify(favoritos_response), 200



def add_favorito(cliente_id):
    cliente = validate_model(Cliente, cliente_id)
    
    data = request.get_json()
    cerveza_id = data.get("cerveza_id")
    
    if not cerveza_id:
        abort(make_response({"message": "cerveza_id is required"}, 400))
    
    cerveza = validate_model(Cerveza, cerveza_id)
    
    favorito = Favoritos(cliente=cliente, cerveza=cerveza)
    db.session.add(favorito)
    db.session.commit()
    
    return jsonify({"message": "Cerveza added to favorites"}), 201
