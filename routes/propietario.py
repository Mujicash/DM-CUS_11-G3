from flask import Blueprint, request, jsonify
from models.propietario import Propietario
from utils.db import db

propietario = Blueprint('propietario', __name__, url_prefix='/api/owner')

@propietario.route("/", methods=['GET'])
def getOwners():
    data = {}
    owners = Propietario.query.all()
    data['Owners'] = [owner.to_json() for owner in owners]

    print(owners)  

    return jsonify(data)

@propietario.route("/add", methods=['POST'])
def addOwner():
    body = request.get_json()

    nombres = body['nombres']
    apellidos = body['apellidos']
    telefono = body['telefono']
    correo = body['correo']

    new_owner = Propietario(nombres, apellidos, telefono, correo)
    db.session.add(new_owner)
    db.session.commit()

    return "saving a new owner"