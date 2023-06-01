from flask import Blueprint, request, jsonify
from models.predio import Predio
from utils.db import db

predio = Blueprint('predio', __name__, url_prefix='/api/predio')

@predio.route("/", methods=['GET'])
def getPredios():
    data = {}
    predios = Predio.query.all()
    data['Predios'] = [predio.to_json() for predio in predios]

    print(data)  

    return jsonify(data)

@predio.route("/add", methods=['POST'])
def addPredio():
    body = request.get_json()

    nombre = body['nombre']
    direccion = body['direccion']
    distrito = body['distrito']
    telefono = body['telefono']
    id_tipo_predio = body['id_tipo_predio']
    print(nombre, direccion)

    nuevo_predio = Predio(nombre, direccion, distrito, telefono, id_tipo_predio)
    db.session.add(nuevo_predio)
    db.session.commit()

    return "saving a new condo"