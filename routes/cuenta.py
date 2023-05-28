from flask import Blueprint, request, jsonify
from models.cuenta import Cuenta
from utils.db import db

cuenta = Blueprint('cuenta', __name__, url_prefix='/api/account')

@cuenta.route("/", methods=['GET'])
def getAccounts():
    data = {}
    accounts = Cuenta.query.all()
    data['Accounts'] = [account.to_json() for account in accounts]

    print(accounts)  

    return jsonify(data)

@cuenta.route("/add", methods=['POST'])
def addAccount():
    body = request.get_json()

    numero = body['numero']
    moneda = body['moneda']
    entidad_bancaria = body['entidad_bancaria']
    id_propietario = body['id_propietario']

    new_account = Cuenta(numero, moneda, entidad_bancaria, id_propietario)
    db.session.add(new_account)
    db.session.commit()

    return "saving a new account"