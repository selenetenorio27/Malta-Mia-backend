from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.encuesta import Encuesta

encuesta_bp = Blueprint("encuesta_bp", __name__, url_prefix="/encuesta")

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message":f"{cls.__name__} {model_id} invalid"}, 400))
    
    model = cls.query.get(model_id)

    if not model:
        abort(make_response({"message":f"{cls.__name__} {model_id} not found"}, 404))
    
    return model

@encuesta_bp.route("", methods=["POST"])
def complete_encuesta():
    data = request.json
    cliente_id = data.get('cliente_id')
    #Aqui se guardara las respuestas de la encuesta en la bd relacionado con el cliente_id
    new_encuesta = Encuesta(cliente_id=cliente_id)
    db.session.add(new_encuesta)
    db.session.commit()
    return jsonify({"message":"Encuesta completada con exito"}), 201