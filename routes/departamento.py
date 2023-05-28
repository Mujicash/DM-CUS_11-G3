from flask import Blueprint, jsonify, request

from models.departamento import Departamento
from utils.db import db

departamento = Blueprint('departamento', __name__, url_prefix='/api/department')

@departamento.route("/", methods=['GET'])
def getDepartments():
    data = {}
    departments = Departamento.query.all()
    data['Departments'] = [department.to_json() for department in departments]

    print(departments)  

    return jsonify(data)

@departamento.route("/add", methods=['POST'])
def addDepartment():
    body = request.get_json()

    piso = body['piso']
    torre = body['torre']
    id_condo = body['id_condo']
    id_owner = body['id_owner']

    new_department = Departamento(piso, torre, id_condo, id_owner)
    db.session.add(new_department)
    db.session.commit()

    return "saving a new department"