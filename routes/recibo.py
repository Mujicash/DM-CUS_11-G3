import datetime

from flask import Blueprint, jsonify, request

from models.recibo import Recibo
from utils.db import db

recibo = Blueprint('recibo', __name__, url_prefix='/api/recibo')

@recibo.route("/", methods=['GET'])
def getRecibos():
    data = {}
    recibos = Recibo.query.all()
    data['Recibos'] = [recibo.to_json() for recibo in recibos]

    print(recibos)  

    return jsonify(data)

@recibo.route("/add", methods=['POST'])
def addRecibo():
    body = request.get_json()

    numero_recibo = body['numero_recibo']
    periodo = body['periodo']
    fecha_vencimiento = datetime.datetime.strptime(body['fecha_vencimiento'], "%d/%m/%Y")
    fecha_emision = datetime.datetime.strptime(body['fecha_emision'], "%d/%m/%Y")
    importe = body['importe']
    ajuste = body['ajuste']
    observacion = body['observacion']
    id_casa = body['id_casa']
    id_recibo_estado = body['id_recibo_estado']

    nuevo_recibo = Recibo(numero_recibo, periodo,fecha_emision, fecha_vencimiento, importe, ajuste, observacion, id_casa, id_recibo_estado)
    db.session.add(nuevo_recibo)
    db.session.commit()

    return "saving a new receipt"