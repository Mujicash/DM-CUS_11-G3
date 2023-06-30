import datetime
import decimal

from flask import Blueprint, jsonify, request
from sqlalchemy import text

from models.recaudacion import Recaudacion
from schemas.recaudacion import recaudaciones_schema
from utils.db import db

recaudaciones = Blueprint("recaudacion", __name__, url_prefix="/api/recaudaciones")


# @recaudaciones.route("/", methods=["GET"])
# def listarRecaudaciones():
#     data = {}
#     recaudaciones = Recaudacion.query.all()
#     data["Recaudaciones"] = [recaudacion.to_json() for recaudacion in recaudaciones]

#     print(recaudaciones)

#     return jsonify(data)


@recaudaciones.route("/", methods=["GET"])
def listarRecaudaciones():
    data = {}
    recaudaciones = Recaudacion.query.all()
    result = recaudaciones_schema.dump(recaudaciones)

    
    data = {
        "recaudaciones": result
    }

    return jsonify(data)



@recaudaciones.route("/", methods=["POST"])
def agregarRecaudacion():
    body = request.get_json()

    id_recaudacion = body["id_recaudacion"]
    id_cuenta = body["id_cuenta"]
    id_mant_recibo = body["id_mant_recibo"]
    n_operacion = body["n_operacion"]
    fecha_operacion = datetime.datetime.strptime(body["fecha_operacion"], "%Y-%m-%d")
    moneda = body["moneda"]
    importe = body["importe"]
    id_recaudacion_estado = body["id_recaudacion_estado"]
    id_cuenta_cargo = body["id_cuenta_cargo"]
    observacion = body["observacion"]

    nueva_recaudacion = Recaudacion(
        id_recaudacion,
        id_cuenta,
        id_mant_recibo,
        n_operacion,
        fecha_operacion,
        moneda,
        importe,
        id_recaudacion_estado,
        id_cuenta_cargo,
        observacion,
    )
    db.session.add(nueva_recaudacion)
    db.session.commit()

    return "saving a new collection"


@recaudaciones.route("/recaudacion-predio/<int:id>", methods=["GET"])
def recaudacionesXPredio(id):
    sql = text(
        "select r.id_recaudacion, TO_CHAR(r.fecha_operacion, 'dd/mm/YYYY') fecha_operacion, tm.etiqueta, r.importe, " +
        "r.id_recaudacion_estado, mt.id_mant_recibo, c.id_casa, c.numero, c.piso, pm.id_predio_mdu, pm.descripcion " + 
        "from recaudacion r " +
        "inner join tipo_moneda tm on r.moneda = tm.id_tipo_moneda " + 
        "inner join mant_recibo mt on r.id_mant_recibo = mt.id_mant_recibo " + 
        "inner join casa c on mt.id_casa = c.id_casa " +
        "inner join predio_mdu pm on c.id_predio_mdu = pm.id_predio_mdu " +
        "where c.id_predio = :id"
    )

    with db.engine.connect() as conn:
        result = conn.execute(sql, {'id': id})
        columns = [key for key in result.keys()]

    recaudaciones = [{columns[index]: r for index, r in enumerate(row)} for row in result]
    
    return jsonify(recaudaciones)

