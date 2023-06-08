from dataclasses import dataclass
from datetime import datetime

from utils.db import db


@dataclass
class Recaudacion(db.Model):

    __tablename__ = 'recaudacion'

    id_transaccion = db.Column(db.Integer, primary_key = True)
    id_cuenta = db.Column(db.Integer, db.ForeignKey('cuenta.id_cuenta'))
    id_mant_recibo = db.Column(db.Integer, db.ForeignKey('recibo.id_recibo'))
    noperacion = db.Column(db.String(25))
    fecha_operacion = db.Column(db.DateTime, nullable=False)
    moneda = db.Column(db.Integer)
    importe = db.Column(db.Float(10,2))
    id_recaudacion_estado = db.Column(db.Integer, db.ForeignKey('recaudacion_estado.id_recaudacion_estado'))
    id_cuenta_cargo = db.Column(db.Integer, db.ForeignKey('cuenta.id'))
    observacion = db.Column(db.String(100))

    def __init__(self, id_mant_recibo, noperacion, fecha_operacion, moneda, 
                 importe, id_recaudacion_estado, id_cuenta_cargo, observacion):
        self.moneda = moneda
        self.importe = importe
        self.id_recaudacion_estado = id_recaudacion_estado
        self.fecha_operacion = fecha_operacion
        self.noperacion = noperacion
        self.observacion = observacion
        self.id_cuenta_cargo = id_cuenta_cargo
        self.id_mant_recibo = id_mant_recibo

    def to_json(self):
        return {
            "id_transaccion": self.id_transaccion,
            "numero_operacion": self.noperacion,
            "fecha_operacion": datetime.strftime(self.fecha_operacion, '%d/%m/%Y'),
            "moneda": self.moneda,
            "importe": self.importe,
            "id_recaudacion_estado": self.id_recaudacion_estado,
            "id_cuenta_cargo": self.id_cuenta_cargo,
            "observacion": self.observacion
        }