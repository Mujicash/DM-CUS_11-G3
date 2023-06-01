from utils.db import db
from dataclasses import dataclass

@dataclass
class Cuenta(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    tipo_cuenta = db.Column(db.String(100))
    numero_cuenta = db.Column(db.String(100))
    moneda = db.Column(db.String(100))
    id_persona = db.Column(db.Integer, db.ForeignKey('persona.id'))
    id_banco = db.Column(db.Integer, db.ForeignKey('banco.id'))

    def __init__(self, tipo_cuenta, numero_cuenta, moneda, id_persona, id_banco):
        self.tipo_cuenta = tipo_cuenta
        self.numero_cuenta = numero_cuenta
        self.moneda = moneda
        self.id_persona = id_persona
        self.id_banco = id_banco

    def to_json(self):
        return {
            "id": self.id,
            "tipo_cuenta": self.tipo_cuenta,
            "numero_cuenta": self.numero_cuenta,
            "moneda": self.moneda,
            "id_persona": self.id_persona,
            "id_banco": self.id_banco
        }