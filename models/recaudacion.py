from dataclasses import dataclass
from datetime import datetime

from utils.db import db


@dataclass
class Recaudacion(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    monto = db.Column(db.Float(10,2))
    fecha_operacion = db.Column(db.DateTime, nullable=False)
    transaccion = db.Column(db.String(25))
    id_cuenta_cargo = db.Column(db.Integer, db.ForeignKey('cuenta.id'))
    id_recibo = db.Column(db.Integer, db.ForeignKey('recibo.id'))

    def __init__(self, monto, fecha_operacion, transaccion, id_cuenta_cargo, id_recibo):
        self.monto = monto
        self.fecha_operacion = fecha_operacion
        self.transaccion = transaccion
        self.id_cuenta_cargo = id_cuenta_cargo
        self.id_recibo = id_recibo

    def to_json(self):
        return {
            "id": self.id,
            "monto": self.monto,
            "fecha_operacion": datetime.strftime(self.fecha_operacion, '%d/%m/%Y'),
            "transaccion": self.transaccion,
            "id_cuenta_cargo": self.id_cuenta_cargo,
            "id_recibo": self.id_recibo
        }