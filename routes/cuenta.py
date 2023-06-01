from flask import Blueprint, request, jsonify
from models.cuenta import Cuenta
from utils.db import db

cuenta = Blueprint('cuenta', __name__, url_prefix='/api/cuenta')

@cuenta.route("/", methods=['GET'])
def getCuentas():
    data = {}
    cuentas = Cuenta.query.all()
    data['Cuentas'] = [cuenta.to_json() for cuenta in cuentas]

    print(cuentas)  

    return jsonify(data)

@cuenta.route("/add", methods=['POST'])
def addCuentas():
    body = request.get_json()

    tipo_cuenta = body['tipo_cuenta']
    numero_cuenta = body['numero_cuenta']
    moneda = body['moneda']
    id_persona = body['id_persona']
    id_banco = body['id_banco']

    nueva_cuenta = Cuenta(tipo_cuenta, numero_cuenta, moneda, id_persona, id_banco)
    db.session.add(nueva_cuenta)
    db.session.commit()

    return "saving a new account"