import datetime

from flask import Blueprint, jsonify, request

from models.recaudacion import Recaudacion
from utils.db import db

recaudacion = Blueprint('recaudacion', __name__, url_prefix='/api/collection')

@recaudacion.route("/", methods=['GET'])
def getCollections():
    data = {}
    collections = Recaudacion.query.all()
    data['Collections'] = [collection.to_json() for collection in collections]

    print(collections)  

    return jsonify(data)

@recaudacion.route("/add", methods=['POST'])
def addCollection():
    body = request.get_json()

    monto = body['monto']
    fecha_operacion = datetime.datetime.strptime(body['fecha_operacion'], "%d/%m/%Y")
    transaccion = body['transaccion']
    id_cuenta_cargo = body['id_cuenta_cargo']
    id_recibo = body['id_recibo']

    new_collection = Recaudacion(monto, fecha_operacion, transaccion, id_cuenta_cargo, id_recibo)
    db.session.add(new_collection)
    db.session.commit()

    return "saving a new collection"