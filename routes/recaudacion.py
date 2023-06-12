import datetime

from flask import Blueprint, jsonify, request

from models.recaudacion import Recaudacion
from utils.db import db

recaudaciones = Blueprint("recaudacion", __name__, url_prefix="/api/recaudaciones")


@recaudaciones.route("/", methods=["GET"])
def listarRecaudaciones():
    data = {}
    recaudaciones = Recaudacion.query.all()
    data["Recaudaciones"] = [recaudacion.to_json() for recaudacion in recaudaciones]

    print(recaudaciones)

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