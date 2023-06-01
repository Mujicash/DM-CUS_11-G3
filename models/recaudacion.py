from dataclasses import dataclass
from datetime import datetime

from utils.db import db


@dataclass
class Recaudacion(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    numero_operacion = db.Column(db.String(25))
    fecha_operacion = db.Column(db.DateTime, nullable=False)
    importe = db.Column(db.Float(10,2))
    observacion = db.Column(db.String(100))
    id_cuenta_cargo = db.Column(db.Integer, db.ForeignKey('cuenta.id'))
    id_recibo = db.Column(db.Integer, db.ForeignKey('recibo.id'))

    def __init__(self, numero_operacion, fecha_operacion, importe, observacion, id_cuenta_cargo, id_recibo):
        self.importe = importe
        self.fecha_operacion = fecha_operacion
        self.numero_operacion = numero_operacion
        self.observacion = observacion
        self.id_cuenta_cargo = id_cuenta_cargo
        self.id_recibo = id_recibo

    def to_json(self):
        return {
            "id": self.id,
            "importe": self.importe,
            "fecha_operacion": datetime.strftime(self.fecha_operacion, '%d/%m/%Y'),
            "numero_operacion": self.numero_operacion,
            "observacion": self.observacion,
            "id_cuenta_cargo": self.id_cuenta_cargo,
            "id_recibo": self.id_recibo
        }