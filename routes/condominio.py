from flask import Blueprint, request, jsonify
from models.condominio import Condominio
from utils.db import db

condominio = Blueprint('condominio', __name__, url_prefix='/api/owner')

@condominio.route("/", methods=['GET'])
def getCondos():
    data = {}
    condos = Condominio.query.all()
    data['Owners'] = [condo.to_json() for condo in condos]

    print(condos)  

    return jsonify(data)

@condominio.route("/add", methods=['POST'])
def addCondo():
    body = request.get_json()

    nombre = body['nombre']
    direccion = body['direccion']

    new_condo = Condominio(nombre, direccion)
    db.session.add(new_condo)
    db.session.commit()

    return "saving a new condo"