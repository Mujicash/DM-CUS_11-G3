import datetime
import decimal

from flask import Blueprint, jsonify, request
from sqlalchemy import text

from models.recaudacion import Recaudacion
from models.recibo import Recibo
from models.casa import Casa
from models.predio_mdu import Predio_Mdu
from schemas.recaudacion import recaudacion_schema, recaudaciones_schema
from utils.db import db

recaudaciones = Blueprint("recaudacion", __name__, url_prefix="/api/recaudaciones")


@recaudaciones.route("/", methods=["GET"])
def listarRecaudaciones():
    data = {}
    recaudaciones = Recaudacion.query.all()
    result = recaudaciones_schema.dump(recaudaciones)

    
    data = {
        "recaudaciones": result
    }

    return jsonify(data)


@recaudaciones.route("/<int:id>", methods=["GET"])
def listarRecaudacion(id):
    data = {}
    recaudaciones = Recaudacion.query.get(id)
    result = recaudacion_schema.dump(recaudaciones)

    
    data = {
        "recaudacion": result
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

    recaudaciones = (
        Recaudacion.query
        .join(Recibo, Recaudacion.id_mant_recibo == Recibo.id_mant_recibo)
        .join(Casa, Recibo.id_casa == Casa.id_casa)
        .join(Predio_Mdu, Casa.id_predio_mdu == Predio_Mdu.id_predio_mdu)
        .filter(Casa.id_predio == id)
        .all()
    )

    # for recaudacion in recaudaciones:
    #     print(recaudacion.id_recaudacion, recaudacion.id_cuenta)

    result = recaudaciones_schema.dump(recaudaciones)

    
    data = {
        "recaudaciones": result
    }
    
    return jsonify(data)