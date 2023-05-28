import datetime

from flask import Blueprint, jsonify, request

from models.recibo import Recibo
from utils.db import db

recibo = Blueprint('recibo', __name__, url_prefix='/api/receipt')

@recibo.route("/", methods=['GET'])
def getReceipts():
    data = {}
    receipts = Recibo.query.all()
    data['Receipts'] = [receipt.to_json() for receipt in receipts]

    print(receipts)  

    return jsonify(data)

@recibo.route("/add", methods=['POST'])
def addReceipts():
    body = request.get_json()

    fecha_vencimiento = datetime.datetime.strptime(body['fecha_vencimiento'], "%d/%m/%Y")
    fecha_emision = datetime.datetime.strptime(body['fecha_emision'], "%d/%m/%Y")
    fecha_pago = datetime.datetime.strptime(body['fecha_pago'], "%d/%m/%Y") if body['fecha_pago'] is not None else body['fecha_pago']
    monto_total = body['monto_total']
    id_departamento = body['id_departamento']

    new_receipt = Recibo(fecha_emision, fecha_vencimiento, fecha_pago, monto_total, id_departamento)
    db.session.add(new_receipt)
    db.session.commit()

    return "saving a new receipt"