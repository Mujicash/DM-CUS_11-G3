from dataclasses import dataclass

from utils.db import db


@dataclass
class Tipo_Moneda(db.Model):

    __tablename__ = 'tipo_moneda'

    id_tipo_moneda = db.Column(db.Integer, primary_key = True)
    descripcion = db.Column(db.String(50))
    etiqueda = db.Column(db.String(4))

    def __init__(self, descripcion, etiqueta):
        self.descripcion = descripcion
        self.etiqueda = etiqueta

    def to_json(self):
        return {
            "id": self.id_tipo_moneda,
            "nombre": self.descripcion,
            "etiqueta": self.etiqueda
        }