from flask import Blueprint, request, jsonify
from models.condominio import Condominio
from utils.db import db

condominio = Blueprint('condominio', __name__, url_prefix='/api/condo')

@condominio.route("/", methods=['GET'])
def getCondos():
    data = {}
    condos = Condominio.query.all()
    data['Condos'] = [condo.to_json() for condo in condos]

    print(data)  

    return jsonify(data)

@condominio.route("/add", methods=['POST'])
def addCondo():
    body = request.get_json()

    nombre = body['nombre']
    direccion = body['direccion']
    distrito = body['distrito']
    telefono = body['telefono']
    print(nombre, direccion)

    new_condo = Condominio(nombre, direccion, distrito, telefono)
    db.session.add(new_condo)
    db.session.commit()

    return "saving a new condo"