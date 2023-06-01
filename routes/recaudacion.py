import datetime

from flask import Blueprint, jsonify, request

from models.recaudacion import Recaudacion
from utils.db import db

recaudacion = Blueprint('recaudacion', __name__, url_prefix='/api/recaudacion')

@recaudacion.route("/", methods=['GET'])
def getRecaudaciones():
    data = {}
    recaudaciones = Recaudacion.query.all()
    data['Recaudaciones'] = [recaudacion.to_json() for recaudacion in recaudaciones]

    print(recaudaciones)  

    return jsonify(data)

@recaudacion.route("/add", methods=['POST'])
def addRecaudacion():
    body = request.get_json()

    importe = body['importe']
    fecha_operacion = datetime.datetime.strptime(body['fecha_operacion'], "%d/%m/%Y")
    numero_operacion = body['numero_operacion']
    observacion = body["observacion"]
    id_cuenta_cargo = body['id_cuenta_cargo']
    id_recibo = body['id_recibo']

    nueva_recaudacion = Recaudacion(numero_operacion, fecha_operacion, importe, observacion, id_cuenta_cargo, id_recibo)
    db.session.add(nueva_recaudacion)
    db.session.commit()

    return "saving a new collection"