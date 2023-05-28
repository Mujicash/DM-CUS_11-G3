from dataclasses import dataclass
from datetime import datetime

from utils.db import db


@dataclass
class Recibo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fecha_emision = db.Column(db.DateTime)
    fecha_vencimiento = db.Column(db.DateTime)
    fecha_pago = db.Column(db.DateTime, nullable=True)
    monto_total = db.Column(db.Float(10,2))
    id_departamento = db.Column(db.Integer, db.ForeignKey('departamento.id'))

    def __init__(self, fecha_emision, fecha_vencimiento, fecha_pago, monto_total, id_departamento):
        self.fecha_emision = fecha_emision
        self.fecha_vencimiento = fecha_vencimiento
        self.fecha_pago = fecha_pago
        self.monto_total = monto_total
        self.id_departamento = id_departamento

    def to_json(self):
        return {
            "id": self.id,
            "fecha_emision": datetime.strftime(self.fecha_emision, '%d/%m/%Y'),
            "fecha_vencimiento": datetime.strftime(self.fecha_vencimiento, '%d/%m/%Y'),
            "fecha_pago": datetime.strftime(self.fecha_pago, '%d/%m/%Y'),
            "monto_total": self.monto_total,
            "id_departamento": self.id_departamento
        }