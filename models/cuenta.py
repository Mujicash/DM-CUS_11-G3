from utils.db import db
from dataclasses import dataclass

@dataclass
class Cuenta(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    numero = db.Column(db.String(100))
    moneda = db.Column(db.String(100))
    entidad_bancaria = db.Column(db.String(100))
    id_propietario = db.Column(db.Integer, db.ForeignKey('propietario.id'))

    def __init__(self, numero, moneda, entidad_bancaria, id_propietario):
        self.numero = numero
        self.moneda = moneda
        self.entidad_bancaria = entidad_bancaria
        self.id_propietario = id_propietario

    def to_json(self):
        return {
            "id": self.id,
            "numero": self.numero,
            "moneda": self.moneda,
            "entidad_bancaria": self.entidad_bancaria,
            "id_propietario": self.id_propietario
        }