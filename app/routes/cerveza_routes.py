from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.cerveza import Cerveza

cervezas_bp = Blueprint("cervezas_bp", __name__, url_prefix="/cervezas")

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message":f"{cls.__name__} {model_id} invalid"}, 400))
    
    model = cls.query.get(model_id)

    if not model:
        abort(make_response({"message":f"{cls.__name__} {model_id} not found"}, 404))
    
    return model


@cervezas_bp.route("", methods=["GET"])
def read_all_cervezas():

    cervezas = Cerveza.query.all()

    cervezas_response = []
    for cerveza in cervezas:
        cervezas_response.append(cerveza.to_dict())
    
    return jsonify(cervezas_response),200


@cervezas_bp.route("/<cerveza_id>", methods=["GET"])
def read_one_cerveza(cerveza_id):
    cerveza = validate_model(Cerveza, cerveza_id)

    return make_response({"cervezas": cerveza.to_dict()})
