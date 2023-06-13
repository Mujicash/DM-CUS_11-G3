import datetime

from flask import Blueprint, jsonify, request
from sqlalchemy import text

from models.recibo import Recibo
from utils.db import db

recibos = Blueprint('recibo', __name__, url_prefix='/api/recibos')

@recibos.route("/", methods=['GET'])
def getRecibos():
    data = {}
    recibos = Recibo.query.all()
    data['Recibos'] = [recibo.to_json() for recibo in recibos]

    print(recibos)  

    return jsonify(data)

@recibos.route("/add", methods=['POST'])
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

@recibos.route("/recibo-tipo-gasto/<int:id>", methods=['GET'])
def mantenimientoReciboTipoGasto(id):

    sql = text(
        "select tg.id_tipo_gasto, tg.descripcion, SUM(mrd.importe_casa) total_tipo_gasto " +
        "from mant_recibo_det mrd " + 
        "inner join gasto g on mrd.id_gasto = g.id_gasto " +
        "inner join tipo_gasto tg on g.id_tipo_gasto = tg.id_tipo_gasto " + 
        "where id_mant_recibo = :id " + 
        "group by tg.id_tipo_gasto"
    )

    with db.engine.connect() as conn:
        result = conn.execute(sql, {'id': id})
        columns = [key for key in result.keys()]

    recaudaciones_tipo_gasto = [{columns[index]: r for index, r in enumerate(row)} for row in result]
    
    return jsonify(recaudaciones_tipo_gasto)