from flask import Blueprint, jsonify, request

from models.persona import Persona
from utils.db import db

persona = Blueprint('persona', __name__, url_prefix='/api/persona')

@persona.route("/", methods=['GET'])
def getPersonas():
    data = {}
    personas = Persona.query.all()
    data['Personas'] = [persona.to_json() for persona in personas]

    print(personas)  

    return jsonify(data)

@persona.route("/add", methods=['POST'])
def addPersona():
    body = request.get_json()

    nombres = body['nombres']
    apellido_paterno = body['apellido_paterno']
    apellido_materno = body['apellido_materno']
    fecha_nacimiento = body['fecha_nacimiento']
    id_tipo_documento = body['id_tipo_documento']
    numero_documento = body['numero_documento']

    nueva_persona = Persona(nombres, apellido_paterno, apellido_materno, fecha_nacimiento, id_tipo_documento, numero_documento)
    db.session.add(nueva_persona)
    db.session.commit()

    return "saving a new person"